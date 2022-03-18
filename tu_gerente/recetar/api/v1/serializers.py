from rest_framework import serializers

from recetar.models import (
  T_Respaldo
)

class TRespaldoSerializer(serializers.ModelSerializer):
  class Meta:
    model = T_Respaldo
    fields = '__all__'