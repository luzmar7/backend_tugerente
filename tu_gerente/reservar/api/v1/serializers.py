from rest_framework import serializers

from reservar.models import (
  Habitacion,
  Cliente
)


class HabitacionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Habitacion
    fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cliente
    fields = '__all__'