from django.contrib import admin

# Register your models here.

from reservar.models import (
  Habitacion,
  Cliente,
  Reserva
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
