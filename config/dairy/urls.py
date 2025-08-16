from django.urls import path

from .views import NoteListView

app_name = 'dairy'  # ✅ это важно!

urlpatterns = [
    path('', NoteListView.as_view(), name='note-list'),
]