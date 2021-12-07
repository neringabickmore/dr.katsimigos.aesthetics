from django.shortcuts import render

from about.models import Contact

# Create your views here.
def view_pricelist(request):
    
    contact_section = Contact.objects.all()

    template = 'pricelist/pricelist.html'

    context = {
        'contact_section': contact_section,
    }

    
    return render (request, template, context)
