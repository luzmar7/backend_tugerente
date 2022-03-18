from django.db import models

# Create your models here.

class T_Respaldo(models.Model):
  id_respaldo = models.AutoField(primary_key = True)
  respaldo = models.CharField(max_length = 20)
  def __str__(self):
    return self.respaldo
  class Meta:
    verbose_name_plural = ("Respaldos")