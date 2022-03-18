from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
  ListaHabitacion,
  ListaCliente,
  ListaReserva
)
app_name = 'reservar'

urlpatterns = [
  path('listaHabitacion/', ListaHabitacion.as_view(), name='ListaHabitacion'),
  path('listaCliente/', ListaCliente.as_view(), name='ListaCliente'),
  path('listaReserva/', ListaReserva.as_view(), name='ListaReserva'),
  ]