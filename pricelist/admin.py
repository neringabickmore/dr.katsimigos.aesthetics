from django.contrib import admin

from .models import PricelistIntro
class PricelistIntroAdmin(admin.ModelAdmin):
    """
    Pricelist Intro Admin
    """

    list_display = (
        'description',
    )

admin.site.register(PricelistIntro, PricelistIntroAdmin)