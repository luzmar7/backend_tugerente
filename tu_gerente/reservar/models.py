from django.db import models
import datetime

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


class Reserva(models.Model):
  ESTADO = (
    ('Pendiente','Pendiente'),
    ('Pagado','Pagado'),
    ('Eliminado','Eliminado')
  )
  id_reserva = models.AutoField(
    primary_key=True,
    verbose_name="Id Reserva"
  )
  id_habitacion = models.ForeignKey(
    Habitacion,
    on_delete=models.CASCADE,
    verbose_name="Habitacion",   
  )
  id_cliente = models.ForeignKey(
    Cliente,
    on_delete=models.CASCADE,
    verbose_name="Cliente",   
  )
  fecha_entrada= models.DateField(
    default=datetime.date.today,
    verbose_name="Fecha de Entrada",
  )
  fecha_salida = models.DateField(
    verbose_name="Fecha de Salida",
    null=True,
    blank = True,
  )
  dias_estadia = models.IntegerField(
    verbose_name="dias estadia",
    null = True
  )
  precio_total = models.DecimalField(
    max_digits=10,
    decimal_places=3,
    verbose_name="precio_total"
  )
  estado = models.CharField(
    max_length = 30, 
    choices = ESTADO, 
    default = 'Pendiente',
    verbose_name="Estado"
  )
  class Meta:
    verbose_name = ("Receta")
    verbose_name_plural = ("Reservas")
  def __int__(self):
    return self.id_receta


class Modo_Pago(models.Model):
  id_modo_pago = models.AutoField(
    primary_key=True,
    verbose_name="Id Modo Pago"
  )
  nombre = models.CharField(
    verbose_name="nombre",
    max_length= 30
  )
  detalles = models.CharField(
    verbose_name="detalles",
    max_length= 30
  )
  def __int__(self):
    return self.id_modo_pago
  class Meta:
    verbose_name_plural = ("Modo_Pago")
    

class Factura(models.Model):
  id_factura = models.AutoField(
    primary_key=True,
    verbose_name="Id Factura"
  )
  id_cliente = models.ForeignKey(
    Cliente,
    on_delete=models.CASCADE,
    verbose_name="Cliente",   
  )
  id_reserva = models.ForeignKey(
    Reserva,
    on_delete=models.CASCADE,
    verbose_name="Reserva",   
  )
  id_modo_pago = models.ForeignKey(
    Modo_Pago,
    on_delete=models.CASCADE,
    verbose_name="modo_pago",   
  )
  fecha= models.DateField(
    default=datetime.date.today,
    verbose_name="Fecha de Entrada",
  )
  def __int__(self):
    return self.id_factura
  class Meta:
    verbose_name_plural = ("Facturas")