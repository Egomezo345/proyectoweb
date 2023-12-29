from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm
# Create your views here.
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import UserProfile

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            # Guardar el usuario
            user = form.save()

            # Crear y guardar el perfil
            profile = UserProfile.objects.create(
                user=user,
                cui=form.cleaned_data['cui'],
                profile_imagen=form.cleaned_data['profile_imagen'],
            )

            return redirect('perfil')  # Redirigir a la página de perfil
    else:
        form = CustomUserCreationForm()

    return render(request, 'registro.html', {'form': form})


class VRegistro(View):

    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, "registro/registro.html", {"form": form})

    def post(self, request):
        form=CustomUserCreationForm(request.POST)

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
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('home')

            else:
                messages.error(request, "usuario no valido")
        else:
            messages.error(request, "informacion incorrecta")

    form=AuthenticationForm()
    return render(request, "login/login.html", {"form": form})