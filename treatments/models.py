from django.db import models
import cloudinary
import cloudinary.uploader

class TreatmentDetails(models.Model):
    """
    A model to specify treatment details
    """
    treatment_name = models.CharField(max_length=150, null=False, blank=False, unique=True)
    description = models.CharField(max_length=1550, null=False, blank=False)
    before_picture = models.ImageField(upload_to='before_picture/', blank=True)
    after_picture = models.ImageField(upload_to='after_picture/', blank=True)
    display = models.BooleanField(default=True)

    def __str__(self):
        return self.description
