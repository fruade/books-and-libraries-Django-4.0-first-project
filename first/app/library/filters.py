import django_filters
from app.library.models import Library


class LibraryFilter(django_filters.FilterSet):
    library_name = django_filters.CharFilter()
    address = django_filters.CharFilter()

    class Meta:
        model = Library
        fields = ['library_name', 'address']