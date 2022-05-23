from contextvars import Context
from django.shortcuts import render
from django.http import HttpResponse
from bdfamilia.models import Familiares
from bdfamilia.templates import *
import datetime

# Create your views here.
#Muestra pagina de inicio de mi WEB
def ingreso(request):
    return render(request,"index.html") 

#Muestra datos contenidos dentro de la BASE DE DATOS
def BDfamiliares(request):
    fam=Familiares.objects.all()
    listafam={"listafam":fam}

    return render(request,"BDfamilia.html",listafam)

#Se realiza el ingreso a Base de Datos de Familiares#
def IngresoFam(request):
    #Familiar 1#
    familiar=Familiares(nombre='Angelica',edad=84,fnac="1938-01-01")
    familiar.save()
    #Familiar 2#
    familiar=Familiares(nombre='Tomas',edad=12,fnac="2010-10-20")
    familiar.save()
    #Familiar 3#
    familiar=Familiares(nombre='Silvano',edad=86,fnac="1936-06-13")
    familiar.save()

    return HttpResponse("Nuevos ingresos en la BD")