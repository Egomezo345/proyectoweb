from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

class VRegistro(View):

    def get(self, request):
        form = UserCreationForm()
        #form=CustomUserCreationForm()
        return render(request, "registro/registro.html", {"form": form})

    def post(self, request):
        pass