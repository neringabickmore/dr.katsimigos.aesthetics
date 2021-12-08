from django.shortcuts import render

from about.models import Contact

# Create your views here.
def view_treatments(request):

    contact_section = Contact.objects.all()
    # Required to show contact details in the footer
    contact_details = Contact.objects.all()
    
    template = 'treatments/treatments.html'

    context = {
        'contact_section': contact_section,
        'contact_details': contact_details,
    }
    
    return render (request, template, context)


def treatment_details(request):

    contact_section = Contact.objects.all()
    # Required to show contact details in the footer
    contact_details = Contact.objects.all()
    
    template = 'treatments/treatment-details.html'

    context = {
        'contact_section': contact_section,
        'contact_details': contact_details,
    }
    
    return render (request, template, context)