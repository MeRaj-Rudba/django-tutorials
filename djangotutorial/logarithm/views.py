from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Entry
from .forms import EntryForm

# Create your views here.
class MyView(View):
    def get(self, request):
        return HttpResponse("Hello, this is MyView!")

class EntryListView(generic.ListView):
    model = Entry
    template_name = 'logarithm/entry_list.html'
    context_object_name = 'entries'

class EntryDetailView(generic.DetailView):
    model = Entry
    template_name = 'logarithm/entry_detail.html'

class EntryCreateView(CreateView):
    model = Entry
    form_class = EntryForm
    template_name = 'logarithm/entry_form.html'
    success_url = reverse_lazy('entry_list')