from django import forms
from app.library.models import Library
from app.library.validators import validation_address


class LibraryForm(forms.ModelForm):
    address = forms.CharField(label='Адрес', validators=[validation_address])

    class Meta:
        model = Library
        fields = ['library_name', 'address', 'contact_phone', 'website_link']