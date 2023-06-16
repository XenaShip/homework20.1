from django.urls import path
from .views import index, contacts, detail


app_name = 'homework'

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('', index, name='index'),
]