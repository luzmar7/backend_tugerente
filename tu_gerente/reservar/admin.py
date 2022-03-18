from django.contrib import admin

# Register your models here.

from reservar.models import (
  Habitacion,
  Cliente,
  Reserva,
  Modo_Pago,
  Factura
)

@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
  list_display = ["id_habitacion", "descripcion", "numero", "piso","precio_dia","estado_habitacion"]

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
  list_display = ["id_cliente", "nombre", "apellido_paterno", "apellido_materno","numero_identificacion","direccion", "telefono", "celular"]

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
  list_display = ["id_reserva", "id_habitacion", "id_cliente", "fecha_entrada","fecha_salida","dias_estadia", "precio_total", "estado"]

@admin.register(Modo_Pago)
class Modo_PagoAdmin(admin.ModelAdmin):
  list_display = ["id_modo_pago", "nombre", "detalles"]

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
  list_display = ["id_factura", "id_cliente", "id_reserva", "id_modo_pago", "fecha"]

