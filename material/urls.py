from django.urls import path

from material.apps import MaterialConfig
from material.views import MaterialCreateView, MaterialListView, MaterialDetailView, MaterialUpdateView, \
    MaterialDeleteView

app_name = MaterialConfig.name

urlpatterns = [
    path('create/', MaterialCreateView.as_view(), name='create'),
    path('', MaterialListView.as_view(), name='list'),
    path('view/<slug:slug>/', MaterialDetailView.as_view(), name='view'),
    path('edit/<slug:slug>/', MaterialUpdateView.as_view(), name='edit'),
    path('delete/<slug:slug>/', MaterialDeleteView.as_view(), name='delete')
]