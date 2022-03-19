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
  Cliente,
  Reserva
)
from .serializers import (
  HabitacionSerializer,
  ClienteSerializer,
  ReservaSerializer,
  ReservaSerializerG
)

#--------- Cliente ---------#
class ListaCliente(APIView):
  def get(self, request):
    cliente = Cliente.objects.all()[:20]
    data = ClienteSerializer(cliente, many=True).data
    return Response(data)

class ClienteGuardar(APIView):
  def get(self, request, format=None):
    snippets = Cliente.objects.all()
    serializer = ClienteSerializer(snippets, many=True)
    return Response(serializer.data)
  def post(self, request, format=None):
    serializer = ClienteSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClienteEditar(APIView):
  def get_object(self, pk):
    try:
      return Cliente.objects.get(id_cliente=pk)
    except Cliente.DoesNotExist:
      raise Http404
  def get(self, request, pk, format=None):
    snippet = self.get_object(pk)
    serializer = ClienteSerializer(snippet)
    return Response(serializer.data)
  def put(self, request, pk, format=None):
    snippet = self.get_object(pk)
    serializer = ClienteSerializer(snippet, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClienteEliminar(APIView):
  def get_object(self, pk):
    try:
      return Cliente.objects.get(id_cliente=pk)
    except Cliente.DoesNotExist:
      raise Http404
  def get(self, request, pk, format=None):
    snippet = self.get_object(pk)
    serializer = ClienteSerializer(snippet)
    return Response(serializer.data)
  def delete(self, request, pk, format=None):
    snippet = self.get_object(pk)
    snippet.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
#--------- End Cliente ---------#

#--------- Habitacion ---------#
class ListaHabitacion(APIView):
  def get(self, request):
    habitacion = Habitacion.objects.all()[:20]
    data = HabitacionSerializer(habitacion, many=True).data
    return Response(data)

class HabitacionGuardar(APIView):
  def get(self, request, format=None):
    snippets = Habitacion.objects.all()
    serializer = HabitacionSerializer(snippets, many=True)
    return Response(serializer.data)
  def post(self, request, format=None):
    serializer = HabitacionSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HabitacionEditar(APIView):
  def get_object(self, pk):
    try:
      return Habitacion.objects.get(id_habitacion=pk)
    except Habitacion.DoesNotExist:
      raise Http404
  def get(self, request, pk, format=None):
    snippet = self.get_object(pk)
    serializer = HabitacionSerializer(snippet)
    return Response(serializer.data)
  def put(self, request, pk, format=None):
    snippet = self.get_object(pk)
    serializer = HabitacionSerializer(snippet, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HabitacionEliminar(APIView):
  def get_object(self, pk):
    try:
      return Habitacion.objects.get(id_habitacion=pk)
    except Habitacion.DoesNotExist:
      raise Http404
  def get(self, request, pk, format=None):
    snippet = self.get_object(pk)
    serializer = HabitacionSerializer(snippet)
    return Response(serializer.data)
  def delete(self, request, pk, format=None):
    snippet = self.get_object(pk)
    snippet.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
#--------- End Habitacion ---------#

#--------- Reserva ---------#
class ListaReserva(APIView):    
  #LISTA TODOS LOS REGISTROS
  def get(self, request, format=None):
    snippets = Reserva.objects.all().order_by('-id_reserva')
    serializer = ReservaSerializer(snippets, many=True)
    return Response(serializer.data)

class ReservaGuardar(APIView):
  def get(self, request, format=None):
    snippets = Reserva.objects.all()
    serializer = ReservaSerializerG(snippets, many=True)
    return Response(serializer.data)
  def post(self, request, format=None):
    serializer = ReservaSerializerG(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReservaEditar(APIView):
  def get_object(self, pk):
    try:
      return Reserva.objects.get(id_reserva=pk)
    except Reserva.DoesNotExist:
      raise Http404
  def get(self, request, pk, format=None):
    snippet = self.get_object(pk)
    serializer = ReservaSerializerG(snippet)
    return Response(serializer.data)
  def put(self, request, pk, format=None):
    snippet = self.get_object(pk)
    serializer = ReservaSerializerG(snippet, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReservaEliminar(APIView):
  def get_object(self, pk):
    try:
      return Reserva.objects.get(id_reserva=pk)
    except Reserva.DoesNotExist:
      raise Http404
  def get(self, request, pk, format=None):
    snippet = self.get_object(pk)
    serializer = ReservaSerializerG(snippet)
    return Response(serializer.data)
  def delete(self, request, pk, format=None):
    snippet = self.get_object(pk)
    snippet.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
#--------- End Reserva ---------#
