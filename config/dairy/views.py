from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views import generic

from .forms import NoteForm
from .models import Note


class NoteListView(generic.ListView):
    model = Note
    template_name = 'dairy/index.html'
    ordering = ['-date']
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['total_notes'] = self.get_queryset().count()
        return ctx


class NoteCreateView(generic.CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'dairy/create_note.html'
    success_url = reverse_lazy('dairy:note-list')


class NoteDeleteView(generic.DeleteView):
    model = Note
    template_name = 'dairy/delete_note.html'
    success_url = reverse_lazy('dairy:note-list')