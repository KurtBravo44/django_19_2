from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, HomeListView, ProductDetailView, MaterialCreateView, MaterialListView, \
    MaterialDetailView, MaterialUpdateView, MaterialDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('create/', MaterialCreateView.as_view(), name='create'),
    path('list/', MaterialListView.as_view(), name='list'),
    path('view/<int:pk>/', MaterialDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', MaterialUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', MaterialDeleteView.as_view(), name='delete')
]