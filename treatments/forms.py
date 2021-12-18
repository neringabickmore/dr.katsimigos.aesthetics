from django import forms
from .widgets import CustomClearableFileInput
from .models import TreatmentDetails

class TreatmentDetailsForm (forms.ModelForm):
    """
    A form to create a new treatment
    """
    class Meta:
        model = TreatmentDetails
        fields = ['treatment_name', 'description', 'before_picture', 'after_picture', 'display']
    
    before_picture = forms.ImageField(
        label='Before picture', required=False,
        widget=CustomClearableFileInput)
    
    after_picture = forms.ImageField(
        label='Before picture', required=False,
        widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        labels = {
            'treatment_name': 'Treatment Name',
            'description': 'Treatment Description',
            'before_picture': 'Upload: Before picture',
            'after_picture': 'Upload: After picture',
            'display': 'Box ticked if you want to display this treatment.'
        }

        for field in self.fields:
            self.fields[field].label = labels[field]
            self.fields['treatment_name'].widget.attrs['class'] = 'field-styling'
            self.fields['description'].widget.attrs['class'] = 'field-styling'
            self.fields['before_picture'].widget.attrs['class'] = 'field-styling'
            self.fields['after_picture'].widget.attrs['class'] = 'field-styling'
            self.fields['display'].widget.attrs['class'] = 'field-styling'

