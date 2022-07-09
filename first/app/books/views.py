from django.http import HttpResponse, Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Book, PublishingHouse, Author
from django.core.exceptions import ObjectDoesNotExist

class BookList(ListView):
    #model = Book
    template_name = 'book_list.html'
    queryset = Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.queryset
        return context


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


class BookInfo(DetailView):
    template_name = 'books/book_info.html'
    model = Book
    pk_url_kwarg = 'pk'
    context_object_name = 'book_details'






