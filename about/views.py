from django.shortcuts import render

# Create your views here.
def view_about(request):
    
    template = 'about/about.html'
    
    return render (request, template)