from os import name
from django.urls import path

from snacks.models import Snack
from .views import SnackListView

urlpatterns = [
    path('', SnackListView.as_view(), name='snack_list' )
]