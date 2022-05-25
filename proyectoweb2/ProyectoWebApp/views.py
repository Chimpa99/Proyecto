from django.shortcuts import render, HttpResponse

from carro.carro import Carro



# Create your views here.

def inicio (request):

    carro=Carro(request)

    return render(request,"ProyectoWebApp/inicio.html")





