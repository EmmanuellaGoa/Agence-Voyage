from django.urls import path
#from django.urls import views
from .views import *
from django.contrib.auth import views # creer une vue de connection prédefinie

urlpatterns =[
    path('', home, name = "home"),
    path('deconnection', deconnection, name = "deconnection"),
    path('register',register, name = "register"),
    path('login',connexion, name = "login"),
    path('destination',destination, name = "destination"),
    path('gallery',gallery, name = "gallery"),
    path('contactUs',contactUs, name = "contactUs"),
     
]
