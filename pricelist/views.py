from django.shortcuts import render

from about.models import Contact
from treatments.models import TreatmentDetails

# Create your views here.
def pricelist(request):
    
    contact_section = Contact.objects.all()
    # Required to show contact details in the footer
    contact_details = Contact.objects.all()
    all_treatments = TreatmentDetails.objects.all()

    template = 'pricelist/pricelist.html'

    context = {
        'contact_section': contact_section,
        'contact_details': contact_details,
        'all_treatments': all_treatments,
    }
    
    return render (request, template, context)
