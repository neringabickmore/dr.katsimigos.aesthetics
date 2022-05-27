from django.db import models
from django.core.validators import MinValueValidator
import cloudinary
import cloudinary.uploader

class TreatmentDetails(models.Model):
    """
    A model to specify treatment details
    """
    class Meta:
        verbose_name_plural = "Treatment Details"

    treatment_name = models.CharField(
        max_length=150, null=False, blank=False, unique=True)
    treatment_description = models.CharField(
        max_length=1550, null=False, blank=False)
    main_picture = models.ImageField(
        upload_to='main_picture/', blank=False)
    before_picture = models.ImageField(
        upload_to='before_picture/', blank=True)
    after_picture = models.ImageField(
        upload_to='after_picture/', blank=True)
    display_treatment = models.BooleanField(default=True, blank=False)
    treatment_price_description = models.CharField(
        max_length=1550, null=True, blank=True)
    price_name_a = models.CharField(
        max_length=150, null=True, blank=False)
    price_a = models.DecimalField(
        max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)], blank=False, null=True)
    price_name_b = models.CharField(
        max_length=150, null=False, blank=True)
    price_b = models.DecimalField(
        max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)], blank=True, null=True)
    price_name_c = models.CharField(
        max_length=150, null=False, blank=True)
    price_c = models.DecimalField(
        max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)], blank=True, null=True)
    price_name_d = models.CharField(
        max_length=150, null=False, blank=True)
    price_d = models.DecimalField(
        max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)], blank=True, null=True)
    price_name_e = models.CharField(
        max_length=150, null=False, blank=True)
    price_e = models.DecimalField(
        max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)], blank=True, null=True)
    price_name_f = models.CharField(
        max_length=150, null=False, blank=True)
    price_f = models.DecimalField(
        max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)], blank=True, null=True)
    price_name_g = models.CharField(
        max_length=150, null=False, blank=True)
    price_g = models.DecimalField(
        max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)], blank=True, null=True)
    price_name_h = models.CharField(
        max_length=150, null=False, blank=True)
    price_h = models.DecimalField(
        max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)], blank=True, null=True)

    def __str__(self):
        return self.treatment_description
