from django.shortcuts import render
from homework.models import Product


# Create your views here.
def index(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, 'homework/catalog2.html', context)


def detail(request, pk):
    product_object = Product.objects.get(pk=pk)
    context = {
        'object': product_object
    }
    return render(request, 'homework/detail.html', context)


def contacts(request):
    return render(request, 'homework/contacts2.html')