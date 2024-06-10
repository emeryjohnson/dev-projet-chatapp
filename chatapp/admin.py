from django.contrib import admin
from .models import Message , Room
# Register your models here.

# dans le fichier admin nous allons representer les classes qui representent les tables de notre base de donnee
# Maintenant l'administrateur a le droit de gerer les donnees des modeles 
admin.site.register(Message)
admin.site.register(Room)
