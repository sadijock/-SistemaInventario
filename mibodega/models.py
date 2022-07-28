from django.db import models
from django.forms import Textarea


# Create your models here.
class Usuario(models.Model):
    codigo_us= models.CharField(primary_key=True, max_length=10)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    # correo=models.EmailField(max_length=50)
    telefono=models.PositiveSmallIntegerField()

    
    #Generar nombre completo
    def nombre_completo(self):
        texto="{0} {1}"
        return texto.format(self.nombre, self.apellido)


    #sobre escribir el metodo to str
    def __str__(self) -> str:
        texto= "{0}(Codigo: {1}) (Telefono: {2}) "
        return texto.format(self.nombre_completo(), self.codigo_us, self.telefono )



class Categoria(models.Model):
    codigo_Categoria= models.CharField(primary_key=True, max_length=6)
    nombre_c=models.CharField(max_length=50)
    

     #sobre escribir el metodo to str

    def __str__(self) -> str:
        txt="{0}  (Codigo de categoria: {1})"
        return txt.format(self.nombre_c, self.codigo_Categoria)

class Inventario(models.Model):
    # codigo_inventario= models.AutoField(primary_key=True)
    codigo_inventario= models.CharField(primary_key=True, max_length=10)
    nombre_p=models.CharField(max_length=50)
    
    precio=models.PositiveSmallIntegerField()
    cantidad=models.PositiveSmallIntegerField()
    # descripcion=models.CharField(max_length=50)
    descripcion=models.TextField()
    cod_us = models.ForeignKey(Usuario, null=False, blank=True,  on_delete=models.CASCADE)
    cod_cat= models.ForeignKey(Categoria, null=False, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        text = "{0}  ({1}$) (Cantidad: {2}) (Usuario: {3}) (Categoria: {4})"
        return text.format(self.nombre_p, self.precio, self.cantidad, self.cod_us, self.cod_cat)
