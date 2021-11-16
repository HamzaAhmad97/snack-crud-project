from os import name
from django.urls import path

from snacks.models import Snack
from .views import SnackListView, SnackDetailView

urlpatterns = [
    path('', SnackListView.as_view(), name='snack_list' ),
    path('snack/<int:pk>/', SnackDetailView.as_view(), name='snack_detail' )
]