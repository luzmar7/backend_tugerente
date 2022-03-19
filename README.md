# backend_tugerente

Mariluz Vargas Hilari

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

-   To create a **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy backend_tugerente

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).

### EXPLICACIÓN ENDPOINTS
La documentancion detalla de la base de datos, flujo de la reserva y los endpoints se encuentran en el archivo /backend_tugerente/tree/master/documentacion

resumen de los endpoints:

reservar/v1/listaCliente/ 
lista todos los clientes del hotel

reservar/v1/ClienteGuardar/ 
realiza el registro de un cliente en el hotel

reservar/v1/ClienteEditar/<int:pk>/ 
realiza la actualizacion de los datos de un cliente del hotel

reservar/v1/ClienteEliminar/<int:pk>/
elimina un ciente del hotel

reservar/v1/ClienteBuscar/<str:busca>/ 
busca en cliente segun su numero de identificacion

reservar/v1/listaHabitacion/
lista todas las habitaciones del hotel

reservar/v1/HabitacionGuardar/
realiza el registro de una habitacion

reservar/v1/HabitacionEditar/<int:pk>/
realiza la actualizacion de datos de una habitacion del hotel

reservar/v1/HabitacionEliminar/<int:pk>/
elimina una habitacion del hotel

reservar/v1/listaReserva/
lista todas las reservas

reservar/v1/ReservaGuardar/
realiza el registro de una reserva

reservar/v1/ReservaEditar/<int:pk>/
realiza la actualizacion de los datos de una reserva

reservar/v1/ReservaEliminar/<int:pk>/
elimina una reserva del hotel

reservar/v1/ReservaBuscar/<str:fecha>/
busca una reserva de una determinada fecha

reservar/v1/listaModoPago/
lista todos los modos de pago

reservar/v1/ModoPagoGuardar/
realiza el registro de un modo de pago

reservar/v1/ModoPagoEditar/<int:pk>/
realiza la actualizacion de datos de un modo de pago

reservar/v1/ModoPagoEliminar/<int:pk>/
elimina un modo de pago

reservar/v1/listaFactura/
lista las facturas

reservar/v1/FacturaGuardar/
realiza el registro de una reserva

reservar/v1/FacturaEditar/<int:pk>/
realiza la actualizacion de datos de una factura

reservar/v1/FacturaEliminar/<int:pk>/
elimina el registro de una factura