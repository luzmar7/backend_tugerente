from rest_framework import serializers

from reservar.models import (
  Habitacion,
  Cliente,
  Reserva
)


class HabitacionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Habitacion
    fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cliente
    fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
  id_cliente = ClienteSerializer(read_only=True)
  id_habitacion = HabitacionSerializer(read_only=True)
  class Meta:
    model = Reserva
    fields = '__all__'