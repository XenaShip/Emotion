from django.core.exceptions import ValidationError
from django.db import models
from django.utils.functional import empty

NULLABLE = {'blank': True, 'null': True}

class Note(models.Model):
    CHOICES = (
        ('😊', 'happy'),
        ('😐', 'okey'),
        ('😢', 'bad')
    )
    mood = models.TextField(max_length=6, choices=CHOICES)
    text_note = models.TextField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)

    def clean(self):
        text = (self.text_note or '').strip()
        if text == '':
            raise ValidationError({'text_note': 'Текст пустой'})
        elif 'дурак' in text.lower():
            raise ValidationError({'text_note': 'Нельзя обзываться!'})





