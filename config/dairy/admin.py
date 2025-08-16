from django.contrib import admin

from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('mood', 'text_note', 'date')
    list_filter =  ('mood',)
    search_fields = ('text_note',)

