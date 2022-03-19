from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
  ListaCliente,
  ClienteGuardar,
  ClienteEditar,
  ClienteEliminar,

  ListaHabitacion,
  HabitacionGuardar,
  HabitacionEditar,
  HabitacionEliminar,

  ListaReserva,
  ReservaGuardar,
  ReservaEditar,
  ReservaEliminar,
)
app_name = 'reservar'

urlpatterns = [

  #--------- Cliente ---------#
  path('listaCliente/', ListaCliente.as_view(), name='ListaCliente'),
  path('ClienteGuardar/', ClienteGuardar.as_view(), name="ClienteGuardar"),
  path('ClienteEditar/<int:pk>/', ClienteEditar.as_view(), name="ClienteEditar"),
  path('ClienteEliminar/<int:pk>/', ClienteEliminar.as_view(), name="ClienteEliminar"),
  #--------- End Cliente ---------#

  #--------- Habitacion ---------#
  path('listaHabitacion/', ListaHabitacion.as_view(), name='ListaHabitacion'),
  path('HabitacionGuardar/', HabitacionGuardar.as_view(), name="HabitacionGuardar"),
  path('HabitacionEditar/<int:pk>/', HabitacionEditar.as_view(), name="HabitacionEditar"),
  path('HabitacionEliminar/<int:pk>/', HabitacionEliminar.as_view(), name="HabitacionEliminar"),
  #--------- End Habitacion ---------#

  #--------- Reserva ---------#
  path('listaReserva/', ListaReserva.as_view(), name='ListaReserva'),
  path('ReservaGuardar/', ReservaGuardar.as_view(), name="ReservaGuardar"),
  path('ReservaEditar/<int:pk>/', ReservaEditar.as_view(), name="ReservaEditar"),
  path('ReservaEliminar/<int:pk>/', ReservaEliminar.as_view(), name="ReservaEliminar"),
  #--------- End Reserva ---------#
  

  ]