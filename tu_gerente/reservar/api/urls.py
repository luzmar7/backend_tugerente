from django.contrib import admin
from django.urls import path, include

app_name = 'reservar'
urlpatterns = [
    path('v1/',include("reservar.api.v1.urls", namespace="v1")),
]
