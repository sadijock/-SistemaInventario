from django.shortcuts import redirect, render
from .models import Categoria, Inventario, Usuario
from  .forms import FormCategoria

# Create your views here.
def home(request):
    return render(request, 'home.html')

def Ge_inventario(request):
    inventario = Inventario.objects.all()
    return render(request, "gestionInventario.html", {"inventarios": inventario})

def registrarInventario(request):
    codigo_i= request.POST['txtCodigo']
    nombre_i= request.POST['txtNombre']
    cantidad_i= request.POST['txtCantidad']
    
    precio_i= request.POST['txtPrecio'] 
    # descripcion_i= request.POST['txtDescripcion']  descripcion=descripcion_i
    
    inventario = Inventario.objects.create(
        codigo_inventario=codigo_i, nombre_p=nombre_i, cantidad=cantidad_i, precio=precio_i  
    )
    return redirect('/gestionInventario/')

def edicionInventario(request, codigo_inventario):
    inventario = Inventario.objects.get(codigo_inventario=codigo_inventario)
    return render(request, "edicionInventario.html", {"inventario": inventario})

def editarInventario(request):
    codigo_i= request.POST['txtCodigo']
    nombre_i= request.POST['txtNombre']
    cantidad_i= request.POST['txtCantidad']
    precio_i= request.POST['txtPrecio']
    # descripcion_i= request.POST['txtDescripcion']

    inventario = Inventario.objects.get(codigo_inventario=codigo_i)

    inventario.codigo_inventario=codigo_i
    inventario.nombre_p=nombre_i
    inventario.cantidad=cantidad_i
    inventario.precio=precio_i
    # inventario.descripcion=descripcion_i
    inventario.save()
    return redirect('/gestionInventario/')

def eliminarInventario(request, codigo_inventario ):
    # para listar los inventarios
    inventario = Inventario.objects.get(codigo_inventario=codigo_inventario)
    inventario.delete()
    return redirect('/gestionInventario/')


def Ge_usuario(request):
    usuario= Usuario.objects.all()
    return render(request, "gestionUsuario.html",{"usuarios": usuario} )

def registrarUsuario(request):
    codigo_u= request.POST['txtCodigo']
    nombre_u= request.POST['txtNombre']
    telefono_u= request.POST['txtTelefono']
    

    usuario = Usuario.objects.create(
        codigo_us=codigo_u, nombre=nombre_u, telefono=telefono_u
    )
    return redirect('/gestionUsuario/')


def edicionUsuario(request, codigo_us):
    # para listar los usuarios
    usuario = Usuario.objects.get(codigo_us=codigo_us)
    return render(request, "edicionUsuario.html", {"usuario": usuario})

def editarUsuario(request):
    codigo_u= request.POST['txtCodigo']
    nombre_u= request.POST['txtNombre']
    telefono_u= request.POST['txtTelefono']
    
    usuario= Usuario.objects.get(codigo_us=codigo_u)

    usuario.codigo_us = codigo_u
    usuario.nombre =nombre_u
    usuario.telefono =telefono_u
    usuario.save()
    return redirect('/gestionUsuario/')

def eliminarUsuario(request, codigo_us):
    usuario = Usuario.objects.get(
        codigo_us=codigo_us)
    usuario.delete()
    return redirect('/gestionUsuario/')


def Ge_categoria(request):
    categoria= Categoria.objects.all()
    return render(request, "gestionCategoria.html",{"categorias": categoria} )

def registarCategoria(request):
    codigo_ca= request.POST['txtCodigo']
    nombre_ca= request.POST['txtNombre']

    recategoria = Categoria.objects.create(
        codigo_Categoria=codigo_ca, nombre_c=nombre_ca
    )
    return redirect('/gestionCategoria/')

def registrarCategoriafull(request):
    # acceder a mi obejto llamarlo 
    formulario = FormCategoria()
    # cargo la vista,  le paso la variable formulario al form para mostrar esa propiedad
    return render(request, 'registrarCategoriafull.html',{
        'form': formulario
    })


def edicionCategoria(request, codigo_Categoria):
    # para listar los usuarios
    categoria = Categoria.objects.get(codigo_Categoria=codigo_Categoria)
    return render(request, "edicionCategoria.html", {"categoria": categoria})


def editarCategoria(request):
    codigo_ca=request.POST['txtCodigo']
    nombre_ca=request.POST['txtNombre']

    categoria = Categoria.objects.get(codigo_Categoria=codigo_ca)

    categoria.codigo_Categoria=codigo_ca
    categoria.nombre_c=nombre_ca
    categoria.save()
    return redirect('/gestionCategoria/')

def eliminarCategoria(request, codigo_Categoria):
    # para listar las categorias
    categoria = Categoria.objects.get(
       codigo_Categoria=codigo_Categoria)
    categoria.delete()
    return redirect('/gestionCategoria/')
