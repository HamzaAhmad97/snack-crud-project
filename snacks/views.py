from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
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
    

    