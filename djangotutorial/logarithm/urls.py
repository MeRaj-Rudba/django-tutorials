from django.urls import path
from .views import EntryListView, EntryDetailView, EntryCreateView

urlpatterns = [
    path('', EntryListView.as_view(), name='entry_list'),
    path('<int:pk>/', EntryDetailView.as_view(), name='entry_detail'),
    path('add/', EntryCreateView.as_view(), name='entry_add'),
]