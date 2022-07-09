from django.http import HttpResponse
from django.shortcuts import render
from .models import Subscription, Library, Reader
from django.db import models


# Create your views here.
def library_start(request):
    # libraries = Subscription.objects.all().values('id_library__library_name',
    #                                               'id_library__address',
    #                                               'id_library__contact_phone',
    #                                               'number_subscription',
    # )
    libraries = Library.objects.all()
    #count_readers = Subscription.objects.all().values('id_library').annotate(n=models.Count("pk"))
    a = libraries[0]
    context = {
        'libraries': libraries,
    }
    return render(request, 'library/book_list.html', context=context)