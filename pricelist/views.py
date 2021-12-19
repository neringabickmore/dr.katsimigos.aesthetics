from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import PricelistIntro
from about.models import Contact
from .forms import PricelistIntroForm
from treatments.models import TreatmentDetails

# Create your views here.
def pricelist(request):
    
    contact_section = Contact.objects.all()
    pricelist_intro_section = PricelistIntro.objects.all()
    # Required to show contact details in the footer
    contact_details = Contact.objects.all()
    all_treatments = TreatmentDetails.objects.all()

    template = 'pricelist/pricelist.html'

    context = {
        'contact_section': contact_section,
        'contact_details': contact_details,
        'all_treatments': all_treatments,
        'pricelist_intro_section': pricelist_intro_section,
    }
    
    return render (request, template, context)


@login_required
def edit_pricelist_intro(request, pricelist_intro_id):
    """
    Edit pricelist section
    """

    if not request.user.is_superuser:
        messages.error(request, 'Functionality available to the site owner only.')
        return redirect(reverse('about'))

    pricelist_intro_section = get_object_or_404(PricelistIntro, pk=pricelist_intro_id)
    # Required to view all treatments on the navbar
    all_treatments = TreatmentDetails.objects.all()
    # Required to show contact details in the footer
    contact_details = Contact.objects.all()
    
    if request.method == 'POST':
        pricelist_intro_form = PricelistIntroForm(request.POST, instance=pricelist_intro_section)
        if pricelist_intro_form.is_valid():
            pricelist_intro_form.save()
            messages.success(request, 'The section updated successfully!')
            return redirect(reverse('pricelist'))
        else:
            messages.error(request, 'Hmmm... something went wrong!')
    else:
        pricelist_intro_form = PricelistIntroForm(instance=pricelist_intro_section)
        messages.info(request, 'You are editing pricelist intro section!')

    template = 'pricelist/edit-intro.html'
    context = {
        'pricelist_intro_form': pricelist_intro_form,
        'pricelist_intro_section': pricelist_intro_section,
        'all_treatments': all_treatments,
        'contact_details': contact_details,
    }

    return render(request, template, context)