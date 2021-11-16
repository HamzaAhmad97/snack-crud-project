from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Snack


class SnackListView(TemplateView):
    model = Snack
    context_object_name = 'snack_list'

class SnackDetailView(DetailView):
    model = Snack
    context_object_name = 'snack_details'

class SnackCreateView(CreateView):
    model = Snack
    fields = ['title', 'purchaser', 'description']
    
class SnackUpdateView(UpdateView):
    model = Snack
    fields = ['title', 'description']

class SnackDeleteView(DeleteView):
    model = Snack
    success_url = reverse_lazy('snack_list')
    