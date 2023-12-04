from django.shortcuts import render, redirect
import json

from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.templatetags.pytils_translit import slugify

from catalog.models import Product, Material


class HomeListView(ListView):
    model = Product
    template_name = 'catalog/home.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'


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


class MaterialCreateView(CreateView):
    model = Material
    fields = ('title', 'body', 'image', 'is_published')
    success_url = reverse_lazy('catalog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)

class MaterialUpdateView(UpdateView):
    model = Material
    fields = ('title', 'body', 'image', 'is_published')
    #success_url = reverse_lazy('catalog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:view', args=[self.kwargs.get('pk')])


class MaterialListView(ListView):
    model = Material

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset

class MaterialDetailView(DetailView):
    model = Material

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object

class MaterialDeleteView(DeleteView):
    model = Material
    success_url = reverse_lazy('catalog:list')

