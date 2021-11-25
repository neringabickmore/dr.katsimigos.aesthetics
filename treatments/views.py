from django.shortcuts import render

# Create your views here.
def view_treatments(request):
    
    template = 'treatments/treatments.html'
    
    return render (request, template)
