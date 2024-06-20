from django.urls import path
from .views import V_registro, cerrar_sesion, logearse

urlpatterns = [
    path('', V_registro.as_view(), name="Autenticacion"),
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),
    path('logearse', logearse, name="logearse"),
]

