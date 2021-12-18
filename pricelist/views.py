from django.shortcuts import render

from about.models import Contact

# Create your views here.
def pricelist(request):
    
    contact_section = Contact.objects.all()
    # Required to show contact details in the footer
    contact_details = Contact.objects.all()

    template = 'pricelist/pricelist.html'

    context = {
        'contact_section': contact_section,
        'contact_details': contact_details,
    }

    
    return render (request, template, context)
