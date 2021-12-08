from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import cloudinary
import cloudinary.uploader
import cloudinary.api

from .models import About, Contact, CarouselPhoto
from .forms import AboutForm, ContactForm, CarouselPhotoForm


# Create your views here.
def view_about(request):

    about_section = About.objects.all()
    contact_section = Contact.objects.all()
    # Required to show contact details in the footer
    contact_details = Contact.objects.all()
    all_carousel_photos = CarouselPhoto.objects.all()
    
    template = 'about/about.html'
    context = {
        'about_section': about_section,
        'contact_section': contact_section,
        'contact_details': contact_details,
        'all_carousel_photos': all_carousel_photos,
    }
    
    return render (request, template, context)


@login_required
def upload_photo(request):

    if not request.user.is_superuser:
        messages.error(request, 'Functionality available to the site owner only.')
        return redirect(reverse('view_about'))

    # Required to show contact details in the footer
    contact_details = Contact.objects.all()


    if request.method == 'POST':
        upload_photo_form = CarouselPhotoForm(request.POST, request.FILES)
        if upload_photo_form.is_valid():
            upload_photo_form.save()
            messages.success(request, 'Successfully added a new photo to the carousel!')
            return redirect('view_about')
        else:
            messages.error(request, 'Failed to add a photo. Please ensure the form is valid.') 

    else:
        upload_photo_form = CarouselPhotoForm()

    template = 'about/upload-photo.html'
    context = {
        'upload_photo_form': upload_photo_form,
        'contact_details': contact_details,
    }
    return render(request, template, context)


@login_required
def edit_about(request, about_id):
    """ Edit about section  """

    if not request.user.is_superuser:
        messages.error(request, 'Functionality available to the site owner only.')
        return redirect(reverse('view_about'))

    about_section = get_object_or_404(About, pk=about_id)
    
    if request.method == 'POST':
        about_form = AboutForm(request.POST, instance=about_section)
        if about_form.is_valid():
            about_form.save()
            messages.success(request, 'The section updated successfully!')
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


@login_required
def edit_contact(request, contact_id):
    """ Edit contact section  """

    if not request.user.is_superuser:
        messages.error(request, 'Functionality available to the site owner only.')
        return redirect(reverse('view_about'))

    contact_section = get_object_or_404(Contact, pk=contact_id)
    # Required to show contact details in the footer
    contact_details = Contact.objects.all()

    if request.method == 'POST':
        contact_form = ContactForm(request.POST, instance=contact_section)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Contact section updated successfully!')
            return redirect(reverse('view_about'))
        else:
            messages.error(request, 'Hmmm... something went wrong!')
    else:
        contact_form = ContactForm(instance=contact_section)
        messages.info(request, 'You are editing contact section!')

    template = 'about/edit-contact-section.html'
    context = {
        'contact_form': contact_form,
        'contact_section': contact_section,
        'contact_details': contact_details,
    }

    return render(request, template, context)