from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import cloudinary
import cloudinary.uploader
import cloudinary.api
from .models import TreatmentDetails
from .forms import TreatmentDetailsForm

from about.models import Contact


def treatments(request):
    """
    view all treatments
    """
    
    contact_section = Contact.objects.all()
    # Required to show contact details in the footer
    contact_details = Contact.objects.all()
    # Required to view all treatments that are activated in the db
    all_treatments = TreatmentDetails.objects.all()
    
    template = 'treatments/treatments.html'

    context = {
        'contact_section': contact_section,
        'contact_details': contact_details,
        'all_treatments': all_treatments,
    }
    
    return render (request, template, context)


def treatment_details(request, name):
    """
    View specific treatment details
    """
    treatment = get_object_or_404(TreatmentDetails, treatment_name=name)
    contact_section = Contact.objects.all()
    # Required to show contact details in the footer
    contact_details = Contact.objects.all()
    
    template = 'treatments/treatment-details.html'

    context = {
        'contact_section': contact_section,
        'contact_details': contact_details,
        'treatment': treatment,
    }
    
    return render (request, template, context)


@login_required
def add_new_treatment(request):
    """
    Superuser can add a new treatment  
    """
    if not request.user.is_superuser:
        messages.error(request, 'Functionality available to the site owner only.')
        return redirect(reverse('treatments'))

    contact_section = Contact.objects.all()
    # Required to show contact details in the footer
    contact_details = Contact.objects.all()

    if request.method == 'POST':
        add_new_treatment_form = TreatmentDetailsForm(request.POST, request.FILES)
        if add_new_treatment_form.is_valid():
            add_new_treatment_form.save()
            messages.success(request, 'Successfully added a new treatment to the database!')
            return redirect('treatments')
        else:
            messages.error(request, 'Failed to add a new treatment. Please ensure the form is valid.') 

    else:
        
        add_new_treatment_form = TreatmentDetailsForm()

    template = 'treatments/add-new-treatment.html'
    context = {
        'add_new_treatment_form': add_new_treatment_form,
        'contact_details': contact_details,
        'contact_section': contact_section,
    }
    return render(request, template, context)


@login_required
def edit_treatment(request, treatment_id):
    """
    Edit treatment details
    """

    if not request.user.is_superuser:
        messages.error(request, 'Functionality available to the site owner only.')
        return redirect(reverse('treatments'))

    treatment_section = get_object_or_404(TreatmentDetails, pk=treatment_id)
    
    if request.method == 'POST':
        treatment_details_form = TreatmentDetailsForm(request.POST, instance=treatment_section)
        if treatment_details_form.is_valid():
            treatment_details_form.save()
            messages.success(request, 'The section updated successfully!')
            return redirect(reverse('treatments'))
        else:
            messages.error(request, 'Hmmm... something went wrong!')
    else:
        treatment_details_form = TreatmentDetailsForm(instance=treatment_section)
        messages.info(request, 'You are editing about section!')

    template = 'treatments/edit-treatment.html'
    context = {
        'treatment_details_form': treatment_details_form,
        'treatment_section': treatment_section
    }

    return render(request, template, context)