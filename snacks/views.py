from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Snack


class SnackListView(TemplateView):
    model = Snack
    context_object_name = 'snack_list'
    template_name = 'snack_list.html'

class SnackDetailView(DetailView):
    model = Snack
    context_object_name = 'snack_details'
    template_name = 'snack_detail.html'

class SnackCreateView(CreateView):
    model = Snack
    fields = ['title', 'purchaser', 'description']
    template_name = 'snack_create.html'
    
class SnackUpdateView(UpdateView):
    model = Snack
    fields = ['title', 'description']
    template_name = 'snack_update.html'

class SnackDeleteView(DeleteView):
    model = Snack
    success_url = reverse_lazy('snack_list')
    template_name = 'snack_delete.html'
    