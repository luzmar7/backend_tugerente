from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
  ListaRespaldo
)
app_name = 'recetar'
urlpatterns = [
	path('listarRespaldo/', ListaRespaldo.as_view(), name='ListaRespaldo')
]
