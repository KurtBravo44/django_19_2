from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView, DetailView, DeleteView, CreateView
from pytils.templatetags.pytils_translit import slugify

from material.models import Material


class MaterialCreateView(CreateView):
    model = Material
    fields = ('title', 'body', 'image', 'is_published')
    success_url = reverse_lazy('material:list')


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
        return reverse('material:view', args=[self.kwargs.get('slug')])


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
    success_url = reverse_lazy('material:list')