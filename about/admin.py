from django.contrib import admin

from .models import About

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

admin.site.register(About, AboutAdmin)