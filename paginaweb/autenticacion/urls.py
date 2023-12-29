from django.urls import path, include

from .views import VRegistro, cerrar_sesion, logear
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', VRegistro.as_view(), name="autenticacion"),

    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),

    path('logear', logear, name="logear"),

]