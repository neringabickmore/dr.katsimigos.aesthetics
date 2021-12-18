from django.contrib import admin
from .models import TreatmentDetails

class TreatmentsAdmin(admin.ModelAdmin):
    """
    ATreatments section admin
    """

    list_display = (
        'treatment_name',
        'description',
        'before_picture',
        'after_picture',
        'display',
    )


admin.site.register(TreatmentDetails, TreatmentsAdmin)