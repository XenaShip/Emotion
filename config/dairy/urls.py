from django.urls import path

from .views import NoteListView, NoteCreateView

app_name = 'dairy'  # ✅ это важно!

urlpatterns = [
    path('', NoteListView.as_view(), name='note-list'),
    path('create/', NoteCreateView.as_view(), name='note-create'),
    path('delete/', NoteDeleteView.as_view(), name='note-delete'),

]