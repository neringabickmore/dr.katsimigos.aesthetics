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


class Contact(models.Model):
    """
    Contact Section Model in About page.
    """

    class Meta:
        verbose_name_plural = "Contact Section"

    header = models.CharField(max_length=254)
    subheader = models.TextField(max_length=254)
    telephone_number = models.CharField(
        max_length=20, null=False, blank=False)
    email_address = models.EmailField(
        max_length=254, null=False, blank=False)
    instagram_handle = models.URLField(
        max_length=1024, default='', null=True, blank=True)
    
    def __str__(self):
        return self.header

