from django.contrib import admin

from .models import About, Contact

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


admin.site.register(About, AboutAdmin)
admin.site.register(Contact, ContactAdmin)