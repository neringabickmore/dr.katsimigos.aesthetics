from django.db import models

class PricelistIntro(models.Model):
    """
    Pricelist Intro model for pricelist page
    """

    class Meta:
        verbose_name_plural = "Pricelist Section"

    description = models.TextField(max_length=10000)
    
    def __str__(self):
        return self.description
