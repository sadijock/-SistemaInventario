#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

"""
iniciar app
django-admin  startproject SistemaInventario
python manage.py startapp mibodega
py manage.py runserver

migracion
python manage.py migrate --> (migracion inicial, me permite crear mi archivo 
de base d datos)
py manage.py makemigrations -->(para realizar las migraciones de mis modelos, q se convierte en 
parte de la base d datos, en tablas)

usuario
super usuario-- para gestionar el panel administrador
py manage.py createsuperuser
nombre del usuario ----> johan97
correo del usuario ---> johandc98@outlook.com
password  --------> 123456
y
---------------Se vuelve volver a correr mi applicacion--------------------

Se puede utilizar siempre el comando migrate y makemigrations para q se guarde los cambios en los modelos

panel de administrador django
http://127.0.0.1:8000/admin

"""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SistemaInventario.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
