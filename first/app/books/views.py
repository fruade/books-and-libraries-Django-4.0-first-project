from django.http import HttpResponse, Http404
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render
from app.books.models import Book, PublishingHouse, Author
from django.core.exceptions import ObjectDoesNotExist
from app.books.forms import BookForm
from app.books.filters import BooksFilter
from django_filters.views import FilterView
from django.urls import reverse_lazy


class BookFormView(CreateView):
    form_class = BookForm
    template_name = 'books/add_book.html'
    success_url = reverse_lazy('books')

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     return super().get_context_data(**kwargs)

    # def form_valid(self, form):
    #     book_object = Book.objects.create(
    #         book_name=form.cleaned_data['book_name'],
    #         description=form.cleaned_data['description'],
    #         id_publishing_house=form.cleaned_data['id_publishing_house'],
    #         date_creation=form.cleaned_data['date_creation'],
    #         book_img=form.cleaned_data['book_img']
    #     )
    #     author = form.cleaned_data['author']
    #     book_object.author.add(*author)
    #     book_object.save()
    #     return super(BookFormView, self).form_valid(form)


class SearchResultsListView(FilterView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/search_results.html'


class BookList(FilterView):
    model = Book
    template_name = 'books/book_list.html'
    filterset_class = BooksFilter
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.model.objects.all()
        return context


class BookInfo(DetailView):
    template_name = 'books/book_info.html'
    model = Book
    pk_url_kwarg = 'pk'
    context_object_name = 'book_details'


# class BookFilter(FilterView):
#     model = Book
#     template_name = 'books/book_list.html'
#     filterset_class = BooksFilter
#     context_object_name = 'books'

# books = Book.objects.all().values('book_name',
#                               'id_publishing_house__publishing_house_name',
#                               'id_publishing_house__address',
#                               'author__first_name',
#                               'author__last_name',
#                               'author__country')

# books = Book.objects.all()
# context = {
#     'books': books,
#     'sale': False,
# }
#
# # return render(requests, 'books/list_books.html', context)
# return render(request, 'books/book_list.html', context)



