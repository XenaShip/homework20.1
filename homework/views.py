from django.shortcuts import render
from homework.models import Product


# Create your views here.
def index(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, 'homework/home.html', context)


def contacts(request):
    return render(request, 'homework/contacts.html')