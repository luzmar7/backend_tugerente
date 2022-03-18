from django.contrib import admin

# Register your models here.

from reservar.models import (
  Habitacion,
  Cliente
)

@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
  list_display = ["id_habitacion", "descripcion", "numero", "piso","precio_dia","estado_habitacion"]

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
  list_display = ["id_cliente", "nombre", "apellido_paterno", "apellido_materno","numero_identificacion","direccion", "telefono", "celular"]
