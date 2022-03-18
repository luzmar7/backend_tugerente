from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render
from rest_framework import status, viewsets

from rest_framework.response import Response
from django.http import HttpResponse
from django.http import Http404 
# Create your views here.
from rest_framework.views import APIView

from django.db.models import Q
from django.db.models import Avg, Count, Min, Sum

from reservar.models import (
  Habitacion,
  Cliente
)
from .serializers import (
  HabitacionSerializer,
  ClienteSerializer
)

class ListaHabitacion(APIView):
  def get(self, request):
    habitacion = Habitacion.objects.all()[:20]
    data = HabitacionSerializer(habitacion, many=True).data
    return Response(data)

class ListaCliente(APIView):
  def get(self, request):
    cliente = Cliente.objects.all()[:20]
    data = ClienteSerializer(cliente, many=True).data
    return Response(data)