from django import forms

from .models import PricelistIntro


class PricelistIntroForm(forms.ModelForm):
    """
    Priselist intro form
    """

    class Meta:
        model = PricelistIntro
        fields = ('description',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        labels = {
            'description': 'Paragraph',

        }
        for field in self.fields:
            self.fields[field].label = labels[field]

        self.fields['description'].widget.attrs['class'] = 'field-styling'