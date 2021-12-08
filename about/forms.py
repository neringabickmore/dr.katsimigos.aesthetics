from django import forms
from .widgets import CustomClearableFileInput
from .models import About, Contact, CarouselPhoto


class AboutForm(forms.ModelForm):
    """
    About form on the home page
    """

    class Meta:
        model = About
        fields = ('name', 'description1', 'description2', 'description3')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description2'].required = False
        self.fields['description3'].required = False
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


class ContactForm(forms.ModelForm):
    """
    Contact form on the home page
    """

    class Meta:
        model = Contact
        fields = ('header', 'subheader', 'telephone_number', 'email_address', 'instagram_handle')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['instagram_handle'].required = False
        self.fields['subheader'].required = False
        labels = {
            'header': 'Header',
            'subheader': 'Subheader',
            'telephone_number': 'Telephone Number',
            'email_address': 'Email Address',
            'instagram_handle': 'Full Instagram Link',

        }
        for field in self.fields:
            self.fields[field].label = labels[field]

        self.fields['header'].widget.attrs['class'] = 'field-styling'
        self.fields['subheader'].widget.attrs['class'] = 'field-styling'
        self.fields['telephone_number'].widget.attrs['class'] = 'field-styling'
        self.fields['email_address'].widget.attrs['class'] = 'field-styling'
        self.fields['instagram_handle'].widget.attrs['class'] = 'field-styling'


class CarouselPhotoForm (forms.ModelForm):

    class Meta:
        model = CarouselPhoto
        fields = '__all__'
    
    image = forms.ImageField(
        label='Image', required=False,
        widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
        labels = {
            'title': 'Title with no spaces',
            'image': 'Upload photo',
        }
        for field in self.fields:
            self.fields[field].label = labels[field]
            self.fields['title'].widget.attrs['class'] = 'field-styling'
            self.fields['image'].widget.attrs['class'] = 'field-styling'
            self.fields['title'].widget.attrs['data-toggle'] = 'tooltip'
            self.fields['title'].widget.attrs['data-placement'] = 'top'
            self.fields['title'].widget.attrs['title'] = 'No spaces \
                or special characters, use - for word separation'