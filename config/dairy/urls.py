from django.urls import path

from .views import NoteListView, NoteCreateView, NoteDeleteView

app_name = 'dairy'

urlpatterns = [
    path('', NoteListView.as_view(), name='note-list'),
    path('create/', NoteCreateView.as_view(), name='note-create'),
    path('delete/', NoteDeleteView.as_view(), name='note-delete'),

]