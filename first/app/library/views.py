from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render
from app.library.models import Subscription, Library, Reader
from django.db import models
from app.library.forms import LibraryForm
from django_filters.views import FilterView
from app.library.filters import LibraryFilter


class LibraryList(FilterView):
    paginate_by = 2
    model = Library
    template_name = 'library/library_list.html'
    filterset_class = LibraryFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['libraries'] = self.model.objects.all()
        return context


class LibraryInfo(DetailView):
    template_name = 'library/library_info.html'
    model = Library
    pk_url_kwarg = 'pk'
    context_object_name = 'library_details'


class LibraryFormView(CreateView):
    form_class = LibraryForm
    template_name = 'library/add_library.html'
    success_url = reverse_lazy('libraries')


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