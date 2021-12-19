from django.contrib import admin
from .models import TreatmentDetails

class TreatmentsAdmin(admin.ModelAdmin):
    """
    Treatments admin
    """

    list_display = (
        'treatment_name',
        'treatment_description',
        'main_picture',
        'before_picture',
        'after_picture',
        'display_treatment',
        'treatment_price_description',
        'price_name_a',
        'price_a',
        'price_name_b',
        'price_b',
        'price_name_c',
        'price_c',
        'price_name_d',
        'price_d',
    )


admin.site.register(TreatmentDetails, TreatmentsAdmin)