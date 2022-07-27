import django_filters
from app.books.models import Book, Author, PublishingHouse


class BooksFilter(django_filters.FilterSet):
    book_name = django_filters.CharFilter()
    author = django_filters.ModelChoiceFilter(queryset=Author.objects.all())

    class Meta:
        model = Book
        exclude = ['book_img']
        fields = ['book_name', 'author']


