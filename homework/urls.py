from django.urls import path
from .views import index, contacts


app_name = 'catalog'

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('', index, name='index'),
]