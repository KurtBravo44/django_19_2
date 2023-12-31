from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
import json

from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm, ModeratorForm
from catalog.models import Product, Version, Category
from catalog.services import get_cached_data
from config.settings import CACHE_ENABLED


def category(request):
    category_list = Category.objects.all()
    get_cached_data('category_list')


    context = {
        'object_list': category_list,
        'title': 'Категории'
    }

    return render(request, 'catalog/categories.html' ,context)


class ProductListView(ListView):
    model = Product


    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['version'] = Version.objects.all()
        return context_data


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')
    login_url = 'users:login'

    permission_required = 'catalog.add_product'


    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)



class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    #form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')
    login_url = 'users:login'

    def get_form_class(self):
        if self.request.user.is_staff:
            return ModeratorForm
        else:
            return ProductForm


    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == "POST":
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data




    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()

        if formset.is_valid():

            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductDetailView(DetailView):
    model = Product


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
    login_url = 'users:login'



def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        data = {'name': name, 'phone': phone, 'message': message}
        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)

    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)


