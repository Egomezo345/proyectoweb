from django.shortcuts import render, HttpResponse

from servicios.models import servicio
# Create your views here.
def home(request):
    return render(request, "paginawebapp/home.html")


def servicios(request):

    servicios=servicio.objects.all()
    return render(request, "paginawebapp/servicios.html", {"servicios": servicios})


def tienda(request):
    return render(request, "paginawebapp/tienda.html")


def blog(request):
    return render(request, "paginawebapp/blog.html")


def contacto(request):
    return render(request, "paginawebapp/contacto.html")