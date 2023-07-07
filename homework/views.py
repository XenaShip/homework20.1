from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from homework.models import Product, Note
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.views.generic.list import ListView
from django.views.generic import TemplateView


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

class ContactsTemplateView(generic.TemplateView):
    template_name = 'homework/contacts2.html'


#class NoteCreateView(generic.CreateView):
#    model = Note
#    fields = ('name', 'the_text', 'image', 'published')
#    success_url = reverse_lazy('homework:blog')


class NoteDetailView(generic.DetailView):
    model = Note

    def get_object(self, queryset=None):
        note = super().get_object()
        note.views_up()
        return note

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Просмотр статьи'
        return context_data


class NoteListView(generic.ListView):
    model = Note


class NoteUpdateView(generic.UpdateView):
    model = Note
    fields = ('name', 'the_text', 'image', 'published')
    extra_context = {
        'title': 'изменить статью'
    }

    def get_success_url(self):
        return reverse('homework:note_detail', args=[*self.kwargs.values()])


class NoteCreateView(generic.CreateView):
    model = Note
    fields = ('name', 'the_text', 'image', 'published')
    success_url = reverse_lazy('homework:blog')
    extra_context = {
        'title': 'Создание статьи'
    }


class NoteDeleteView(generic.DeleteView):
    model = Note
    success_url = reverse_lazy('homework:blog')
