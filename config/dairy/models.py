from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Note(models.Model):
    CHOICES = (
        ('😊', 'happy'),
        ('😐', 'okey'),
        ('😢', 'bad')
    )
    mood = models.TextField(max_length=6, choices=CHOICES)
    text_note = models.TextField(max_length=250)
    date = models.DateTimeField(auto_created=True)



