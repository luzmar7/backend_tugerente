from django.contrib import admin

# Register your models here.

from recetar.models import (
 T_Respaldo
)

@admin.register(T_Respaldo)
class t_RespaldoAdmin(admin.ModelAdmin):
  list_display = ["id_respaldo", "respaldo"]
