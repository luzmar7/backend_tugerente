# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from django.http import HttpResponse
from django.http import Http404 
# Create your views here.
from rest_framework.views import APIView
from recetar.models import (
  T_Respaldo
)
from .serializers import (
  TRespaldoSerializer
)

from django.db.models import Q
from django.db.models import Avg, Count, Min, Sum

class ListaRespaldo(APIView):
  def get(self, request):
    respaldo = T_Respaldo.objects.all()[:20]
    data = TRespaldoSerializer(respaldo, many=True).data
    return Response(data)
