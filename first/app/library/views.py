from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Subscription, Library, Reader
from django.db import models


class LibraryList(ListView):
    model = Library
    template_name = 'library_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['libraries'] = self.model.objects.all()
        return context


class LibraryInfo(DetailView):
    template_name = 'library/library_info.html'
    model = Library
    pk_url_kwarg = 'pk'
    context_object_name = 'library_details'


# def library_start(request):
#     # libraries = Subscription.objects.all().values('id_library__library_name',
#     #                                               'id_library__address',
#     #                                               'id_library__contact_phone',
#     #                                               'number_subscription',
#     # )
#     libraries = Library.objects.all()
#     context = {
#         'libraries': libraries,
#     }
#     return render(request, 'library/library_list.html', context=context)