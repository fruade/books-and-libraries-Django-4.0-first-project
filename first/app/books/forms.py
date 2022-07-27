from django import forms
from django.contrib.auth.models import User
from django.contrib.admin import widgets
from app.books.models import Book, Author, PublishingHouse
from app.books.validators import validation_book_name


class BookForm(forms.ModelForm):
    book_name = forms.CharField(label='Название книги', validators=[validation_book_name])
    # author_query = Author.objects.all()
    # author_array = (
    #     [author.id, author] for author in author_query
    # )
    # book_name = forms.CharField(label='Название книги', min_length=1, max_length=50)
    # author = forms.MultipleChoiceField(
    #     widget=forms.CheckboxSelectMultiple(),
    #     choices=author_array,
    #     label='Выберите автора(ов)'
    # )
    # description = forms.CharField(label='Описание книги', widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}))
    # id_publishing_house = forms.ModelChoiceField(label='Издательство', queryset=PublishingHouse.objects.all())
    # date_creation = forms.DateField(label='Дата написания книги')
    # book_img = forms.ImageField(label='Ссылка на изображение', required=False)

    class Meta:
        model = Book
        fields = ['book_name', 'author', 'description', 'id_publishing_house', 'date_creation', 'book_img']
        widgets = {
            'author': forms.CheckboxSelectMultiple()
        }





