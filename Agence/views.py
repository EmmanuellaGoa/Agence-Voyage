from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model,login,logout,authenticate

# Create your views here.
def home(request):
    return render(request, 'home.html')

def connexion(request):
    if request.method == "POST":
      #connecter l'utilisateur
      username = request.POST.get("username")
      password = request.POST.get("password")

      user= authenticate(username=username, password=password)
      if user: #si le user existe
        login(request, user)
        return redirect('home')

    return render(request, 'login.html')    



#recuperer ma class utilisateur
User =  get_user_model()

def register(request):
    if request.method == "POST":
        #traiter le formulaire
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username, password=password) #creer le user ds la bd
        login(request, user) #lui permettre de se connecter a la pg
        return redirect('home')

    return render(request, 'register.html')

def deconnection(request):
    logout(request)
    return redirect('home')

def destination(request):
    return render(request,'destination.html')

def gallery(request):
    return render(request,'gallery.html')


def contactUs(request):
    return render(request,'contactUs.html')