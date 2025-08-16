from django.urls import reverse_lazy
from django.views import generic

from .models import Note


class NoteMain(generic.ListView):
    model = Note
    template_name = 'dairy/index.html'
    def get(self, request):



