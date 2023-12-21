from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.

class VRegistro(View):

    def get(self, request):
        form = UserCreationForm()
        return render(request, "registro/registro.html", {"form": form})

    def post(self, request):
        form=UserCreationForm(request.POST)

        if form.is_valid():

            usuario=form.save()

            login(request, usuario)

            return redirect('home')

        else:
            return render(request, "registro/registro.html", {"form": form})

def cerrar_sesion(request):
    logout(request)

    return redirect('home')

def logear(request):
    form=AuthenticationForm()
    return render(request, "login/login.html", {"form": form})