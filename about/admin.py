from django.contrib import admin

from .models import About, Contact, CarouselPhoto

class AboutAdmin(admin.ModelAdmin):
    """
    About section admin
    """

    list_display = (
        'name',
        'description1',
        'description2',
        'description3',
    )


class ContactAdmin(admin.ModelAdmin):
    """
    Contact section admin
    """

    list_display = (
        'header',
        'subheader',
        'telephone_number',
        'email_address',
        'instagram_handle',
    )


class CarouselPhotoAdmin(admin.ModelAdmin):
    """
    Carousel Photo admin
    """

    list_display = (
        'title',
        'image',
    )

admin.site.register(About, AboutAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(CarouselPhoto, CarouselPhotoAdmin)