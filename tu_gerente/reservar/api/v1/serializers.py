from rest_framework import serializers

from reservar.models import (
  Habitacion,
  Cliente,
  Reserva,
  Modo_Pago,
  Factura
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

class ReservaSerializerG(serializers.ModelSerializer):
  class Meta:
    model = Reserva
    fields = '__all__'

    
class ModoPagoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Modo_Pago
    fields = '__all__'

class FacturaSerializer(serializers.ModelSerializer):
  id_cliente = ClienteSerializer(read_only=True)
  id_reserva = ReservaSerializer(read_only=True)
  id_modo_pago = ModoPagoSerializer(read_only=True)
  class Meta:
    model = Factura
    fields = '__all__'

class FacturaSerializerG(serializers.ModelSerializer):
  class Meta:
    model = Factura
    fields = '__all__'