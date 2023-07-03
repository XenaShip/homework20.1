from django.urls import path
from .views import contacts, ProductListView, ProductDetailView, ProductCreateView, NoteListView, NoteUpdateView, \
    NoteDetailView, NoteCreateView, NoteDeleteView

app_name = 'homework'

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('', ProductListView.as_view(), name='index'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('blog/', NoteListView.as_view(), name='blog'),
    path('update_note/', NoteUpdateView.as_view(), name='update_note'),
    path('create_note/', NoteCreateView.as_view(), name='create_note'),
    path('note_delete/<int:pk>/', NoteDeleteView.as_view(), name='note_delete'),
    path('note_detail/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
]