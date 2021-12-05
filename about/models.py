from django.db import models

class About(models.Model):
    """
    About Section Model for About page
    """

    class Meta:
        verbose_name_plural = "About Section"

    name = models.CharField(max_length=254)
    description1 = models.TextField(max_length=10000)
    description2 = models.TextField(max_length=10000)
    description3 = models.TextField(max_length=10000)
    
    def __str__(self):
        return self.name

