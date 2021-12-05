from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import About
from .forms import AboutForm


# Create your views here.
def view_about(request):

    about_section = About.objects.all()
    
    template = 'about/about.html'
    context = {
        'about_section': about_section,
    }
    
    return render (request, template, context)


@login_required
def edit_about(request, about_id):
    """ Edit about section  """

    if not request.user.is_superuser:
        messages.error(request, 'Functionality available to the site owner only.')
        return redirect(reverse('bio'))

    about_section = get_object_or_404(About, pk=about_id)
    # shows social icons in a footer
    
    if request.method == 'POST':
        about_form = AboutForm(request.POST, instance=about_section)
        if about_form.is_valid():
            about_form.save()
            messages.success(request, 'Section edited successfully!')
            return redirect(reverse('view_about'))
        else:
            messages.error(request, 'Hmmm... something went wrong!')
    else:
        about_form = AboutForm(instance=about_section)
        messages.info(request, 'You are editing about section!')

    template = 'about/edit-about.html'
    context = {
        'about_form': about_form,
        'about_section': about_section,
    }

    return render(request, template, context)