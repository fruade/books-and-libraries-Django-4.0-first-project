from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedBackForm
from .models import FeedBack
from django.urls import reverse
from django.views.generic import FormView
# Create your views here.


class FeedBackView(FormView):
    form_class = FeedBackForm
    template_name = 'feedback/feedback.html'
    success_url = '/feedback/done'

    def form_valid(self, form):
        feed = FeedBack(
            name=form.cleaned_data['name'],
            surname=form.cleaned_data['surname'],
            rating=form.cleaned_data['rating'],
            feedback=form.cleaned_data['feedback'],
        )
        feed.save()
        return super(FeedBackView, self).form_valid(form)

def get_feedback(request):
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            feed = FeedBack(
                name=form.cleaned_data['name'],
                surname=form.cleaned_data['surname'],
                rating=form.cleaned_data['rating'],
                feedback=form.cleaned_data['feedback'],
            )
            feed.save()
            return HttpResponseRedirect('/feedback/done')
    else:
        form = FeedBackForm()
    return render(request, 'feedback/feedback.html', context={'form': form})


def done(request):
    return render(request, 'feedback/done.html')