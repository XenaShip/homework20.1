from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from homework.models import Product, Note
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.views.generic.list import ListView


class ProductListView(generic.ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Список товаров'
        return context_data
# Create your views here.


class ProductDetailView(generic.DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = context_data['object']
        return context_data


class ProductCreateView(generic.CreateView):
    model = Product
    fields = ('name_product', 'price',  'description', 'category',)
    success_url = reverse_lazy('homework:index')
    extra_context = {
        'title': 'Создание продукта'
    }


def contacts(request):
    return render(request, 'homework/contacts2.html')


class NoteCreateView(generic.CreateView):
    model = Note
    fields = ('name', 'the_text', 'image', 'published')


class NoteListView(generic.DetailView):
    model = Note

    def get_object(self, queryset=None):
        note = super().get_object()
        note.views_up()
        return note

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Просмотр статьи'
        return context_data




