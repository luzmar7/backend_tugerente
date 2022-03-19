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

  ListaModoPago,
  ModoPagoGuardar,
  ModoPagoEditar,
  ModoPagoEliminar,

  ListaFactura,
  FacturaGuardar,
  FacturaEditar,
  FacturaEliminar
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

  #--------- Reserva ---------#
  path('listaReserva/', ListaReserva.as_view(), name='ListaReserva'),
  path('ReservaGuardar/', ReservaGuardar.as_view(), name="ReservaGuardar"),
  path('ReservaEditar/<int:pk>/', ReservaEditar.as_view(), name="ReservaEditar"),
  path('ReservaEliminar/<int:pk>/', ReservaEliminar.as_view(), name="ReservaEliminar"),
  #--------- End Reserva ---------#
  
  #--------- Modo_Pago ---------#
  path('listaModoPago/', ListaModoPago.as_view(), name='ListaModoPago'),
  path('ModoPagoGuardar/', ModoPagoGuardar.as_view(), name="ModoPagoGuardar"),
  path('ModoPagoEditar/<int:pk>/', ModoPagoEditar.as_view(), name="ModoPagoEditar"),
  path('ModoPagoEliminar/<int:pk>/', ModoPagoEliminar.as_view(), name="ModoPagoEliminar"),
  #--------- End Modo_Pago ---------#

  #--------- Factura ---------#
  path('listaFactura/', ListaFactura.as_view(), name='ListaFactura'),
  path('FacturaGuardar/', FacturaGuardar.as_view(), name="FacturaGuardar"),
  path('FacturaEditar/<int:pk>/', FacturaEditar.as_view(), name="FacturaEditar"),
  path('FacturaEliminar/<int:pk>/', FacturaEliminar.as_view(), name="FacturaEliminar"),
  #--------- End Factura ---------#

  ]