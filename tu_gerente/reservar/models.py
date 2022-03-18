from django.db import models

# Create your models here.
class Habitacion(models.Model):
  ESTADO = (
    ('Bueno','Bueno'),
    ('Regular','Regular')
  )
  id_habitacion = models.AutoField(
    primary_key=True,
    verbose_name="Id Habitacion"
  )
  descripcion = models.CharField(
    verbose_name="descripcion",
    max_length=200,
    null=True,
    blank = True,
  )
  numero = models.PositiveIntegerField(
    verbose_name="numero"
  )
  piso = models.PositiveIntegerField(
    verbose_name="piso"
  )
  precio_dia = models.DecimalField(
    max_digits=10,
    decimal_places=3,
    verbose_name="precio_dia"
  )
  estado_habitacion = models.CharField(
    max_length = 30, 
    choices = ESTADO, 
    default = 'Bueno',
    verbose_name="estado"
  )
  def __int__(self):
    return self.id_habitacion
  class Meta:
    verbose_name_plural = ("Habitaciones")

class Cliente(models.Model):
  id_cliente = models.AutoField(
    primary_key=True,
    verbose_name="Id Cliente"
  )
  nombre = models.CharField(
    verbose_name="nombre",
    max_length= 30
  )
  apellido_paterno = models.CharField(
    verbose_name="Apellido Paterno",
    max_length = 50
  )
  apellido_materno = models.CharField(
    verbose_name="Apellido Materno",
    max_length = 50
  )
  numero_identificacion = models.CharField(
    verbose_name="numero de identificacion",
    max_length = 15
  )
  direccion = models.CharField(
    verbose_name="direccion",
    max_length = 100
  )
  telefono = models.IntegerField(
    verbose_name="telefono",
    null = True
  )
  celular = models.IntegerField(
    verbose_name="celular",
    null = True
  )
  def __int__(self):
    return self.id_cliente
  class Meta:
    verbose_name_plural = ("Clientes")