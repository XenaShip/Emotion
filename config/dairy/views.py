from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views import generic

from .models import Note


class NoteListView(generic.ListView):
    model = Note
    template_name = 'dairy/index.html'