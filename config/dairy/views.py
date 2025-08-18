from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views import generic

from .forms import NoteForm
from .models import Note


class NoteListView(generic.ListView):
    model = Note
    template_name = 'dairy/index.html'


class NoteCreateView(generic.CreateView):
    model = Note
    form = NoteForm
    template_name = 'dairy/create_note.html'


class NoteDeleteView(generic.DeleteView):
    model = Note
    template_name = 'dairy/delete_note.html'