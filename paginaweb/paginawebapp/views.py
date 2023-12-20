from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    return render(request, "paginawebapp/home.html")


def tienda(request):
    return render(request, "paginawebapp/tienda.html")




def contacto(request):
    return render(request, "paginawebapp/contacto.html")