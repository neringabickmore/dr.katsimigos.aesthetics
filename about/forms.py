from django import forms
from .models import About


class AboutForm(forms.ModelForm):
    """
    About form on the home page
    """

    class Meta:
        model = About
        fields = ('name', 'description1', 'description2', 'description3')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        labels = {
            'name': 'Section title',
            'description1': 'Paragraph 1',
            'description2': 'Paragraph 2',
            'description3': 'Paragraph 3',

        }
        for field in self.fields:
            self.fields[field].label = labels[field]

        self.fields['name'].widget.attrs['class'] = 'field-styling'
        self.fields['description1'].widget.attrs['class'] = 'field-styling'
        self.fields['description2'].widget.attrs['class'] = 'field-styling'
        self.fields['description3'].widget.attrs['class'] = 'field-styling'