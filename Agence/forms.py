"""from django import forms
from django.forms import fields #import de champ"""
from .models import utilisateur


#creation du formulaire
#class AgenceRegistration(forms.ModelForm):
"""    class Meta:
        model = User
        fields = ['prenom', 'nom', 'password']
        
        #bien cadrer le formulaire
        widgets = {
            'prenom': forms.TextInput(attrs= {'class': 'form-control'}),
            'nom': forms.TextInput(attrs= {'class': 'form-control'}),
            'password': forms.PasswordInput(attrs= {'class': 'form-control'}),
            #PasswordInput: chiffrer mdp , attrs: atribut
        }"""


#page de connexion
