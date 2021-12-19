from django import forms
from .widgets import CustomClearableFileInput
from .models import TreatmentDetails

class TreatmentDetailsForm (forms.ModelForm):
    """
    A form to create a new treatment
    """
    class Meta:
        model = TreatmentDetails
        fields = [
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
        ]
    
    main_picture = forms.ImageField(
        label='Main picture', required=True,
        widget=CustomClearableFileInput)

    before_picture = forms.ImageField(
        label='Before picture', required=False,
        widget=CustomClearableFileInput)
    
    after_picture = forms.ImageField(
        label='Before picture', required=False,
        widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        labels = {
            'treatment_name': 'Treatment name',
            'treatment_description': 'Treatment description',
            'main_picture': 'Upload: Main treatment picture',
            'before_picture': 'Upload: Before picture (optional)',
            'after_picture': 'Upload: After picture (optional)',
            'display_treatment': 'Box ticked if you want to display this treatment.',
            'treatment_price_description': 'Treatment price description (optional)',
            'price_name_a': 'Enter price name',
            'price_a': 'Enter the price',
            'price_name_b': 'Enter price name (optional)',
            'price_b': 'Enter the price (optional)',
            'price_name_c': 'Enter price name (optional)',
            'price_c': 'Enter the price (optional)',
            'price_name_d': 'Enter price name (optional)',
            'price_d': 'Enter the price (optional)',
        } 

        for field in self.fields:
            self.fields[field].label = labels[field]
            self.fields['treatment_name'].widget.attrs['class'] = 'field-styling'
            self.fields['treatment_description'].widget.attrs['class'] = 'field-styling'
            self.fields['main_picture'].widget.attrs['class'] = 'field-styling'
            self.fields['before_picture'].widget.attrs['class'] = 'field-styling'
            self.fields['after_picture'].widget.attrs['class'] = 'field-styling'
            self.fields['display_treatment'].widget.attrs['class'] = 'field-styling'
            self.fields['treatment_price_description'].widget.attrs['class'] = 'field-styling'
            self.fields['price_name_a'].widget.attrs['class'] = 'field-styling'
            self.fields['price_a'].widget.attrs['class'] = 'field-styling'
            self.fields['price_name_b'].widget.attrs['class'] = 'field-styling'
            self.fields['price_b'].widget.attrs['class'] = 'field-styling'
            self.fields['price_name_c'].widget.attrs['class'] = 'field-styling'
            self.fields['price_c'].widget.attrs['class'] = 'field-styling'
            self.fields['price_name_d'].widget.attrs['class'] = 'field-styling'
            self.fields['price_d'].widget.attrs['class'] = 'field-styling'

