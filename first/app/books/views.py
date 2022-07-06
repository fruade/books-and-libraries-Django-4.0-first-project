from django.http import HttpResponse
from django.shortcuts import render
from .models import Book, PublishingHouse, Author


def get_books_list(request):
    # books = Book.objects.all().values('book_name',
    #                               'id_publishing_house__publishing_house_name',
    #                               'id_publishing_house__address',
    #                               'author__first_name',
    #                               'author__last_name',
    #                               'author__country')

    # books = Book.objects.all().values('book_name', 'date_creation', 'description',
    #                                   'id_publishing_house__publishing_house_name',
    #                                   'id_publishing_house__address',
    #                                   'id_publishing_house__contact_phone',
    #                                   'id_publishing_house__email',
    #                                   'id_publishing_house__website_link'
    #                                   )
    books = Book.objects.all()
    context = {
        'books': books,
        'sale': False,
    }

    # return render(requests, 'books/list_books.html', context)
    return render(request, 'books/index.html', context)


def get_books_id(request, id_book):
    books = Book.objects.get(id=id_book)
    return books
