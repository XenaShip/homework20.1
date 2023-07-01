from django.urls import path
from .views import contacts, ProductListView, ProductDetailView, ProductCreateView, NoteListView, NoteCreateView


app_name = 'homework'

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('', ProductListView.as_view(), name='index'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('blog/', NoteListView.as_view(), name='blog'),
]