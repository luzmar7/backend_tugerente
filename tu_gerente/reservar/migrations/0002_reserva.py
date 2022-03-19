# Generated by Django 4.0.3 on 2022-03-18 21:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id_reserva', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Reserva')),
                ('fecha_entrada', models.DateField(default=datetime.date.today, verbose_name='Fecha de Entrada')),
                ('fecha_salida', models.DateField(blank=True, null=True, verbose_name='Fecha de Salida')),
                ('dias_estadia', models.IntegerField(null=True, verbose_name='dias estadia')),
                ('precio_total', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='precio_total')),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Pagado', 'Pagado'), ('Eliminado', 'Eliminado')], default='Pendiente', max_length=30, verbose_name='Estado')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservar.cliente', verbose_name='Cliente')),
                ('id_habitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservar.habitacion', verbose_name='Habitacion')),
            ],
            options={
                'verbose_name': 'Receta',
                'verbose_name_plural': 'Recetas',
            },
        ),
    ]