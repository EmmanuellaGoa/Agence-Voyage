from django.db import models
from django.contrib.auth.models import AbstractUser #permet de creer un formlaire perso

# Create your models here.
#class User(models.Model):
 #   prenom = models.CharField(max_length= 70)
    #CharField : champ de caractere longueur 70
#    nom = models.CharField(max_length= 70)
 #   password = models.CharField(max_length= 100) 


class utilisateur (AbstractUser):
    pass