from itertools import product
from django.shortcuts import render
from .models import Producto

# Create your views here.

def tienda (request):

    productos=Producto.objects.all()

    return render(request,"tienda/tienda.html",{"productos":productos})

def producto(request,categoria_id):

    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)
    return render (request, "blog/categoria.html",{'categoria':categoria})