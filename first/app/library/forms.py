from django import forms
from app.library.models import Library


class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = ['library_name', 'address', 'contact_phone', 'website_link']