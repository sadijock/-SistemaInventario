"""SistemaInventario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path

from mibodega.views import Ge_inventario,  Ge_usuario, home, registrarInventario, Ge_categoria, registrarUsuario, registarCategoria, eliminarUsuario, edicionUsuario, editarUsuario, edicionCategoria, editarCategoria, eliminarCategoria,editarInventario, edicionInventario, eliminarInventario, registrarCategoriafull
# from mibodega import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('gestionUsuario/', Ge_usuario, name="index"),

    path('gestionInventario/', Ge_inventario, name="inventario"),  
    path('registrarInventario/', registrarInventario ), 
    path('gestionInventario/edicionInventario/<codigo_inventario>', edicionInventario ),
    path('editarInventario/', editarInventario), 
    path('gestionInventario/eliminarInventario/<codigo_inventario>', eliminarInventario ),

    path('gestionUsuario/', Ge_usuario, name="usuario"),
    path('registrarUsuario/', registrarUsuario ),
    path('gestionUsuario/edicionUsuario/<codigo_us>', edicionUsuario ),
    path('editarUsuario/', editarUsuario ),
    path('gestionUsuario/eliminarUsuario/<codigo_us>', eliminarUsuario ),   

    path('gestionCategoria/', Ge_categoria, name="categoria"),
    path('registrarCategoria/', registarCategoria),    
    path('gestionCategoria/edicionCategoria/<codigo_Categoria>', edicionCategoria),
    path('editarCategoria/', editarCategoria ), 
    path('gestionCategoria/eliminarCategoria/<codigo_Categoria>', eliminarCategoria),
    path('registrarCategoriafull/', registrarCategoriafull, name="categoriafull"),


]

