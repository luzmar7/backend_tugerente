from django.contrib import admin
from django.urls import path, include

app_name = 'recetar'
urlpatterns = [
    path('v1/',include("recetar.api.v1.urls", namespace="v1"))
]
