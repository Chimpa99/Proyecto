from email.headerregistry import ContentDispositionHeader
from ssl import create_default_context
from tabnanny import verbose
from tkinter import image_names
from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo=models.CharField(max_length=50)
    Contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='servicios') 
    created=models.DateTimeField(auto_now_add=True) 
    updated=models.DateTimeField(auto_now_add=True) 

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'

def __str__(self):
    return self.titulo
