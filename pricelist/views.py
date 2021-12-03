from django.shortcuts import render

# Create your views here.
def view_pricelist(request):
    
    template = 'pricelist/pricelist.html'
    
    return render (request, template)
