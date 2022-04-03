from django.shortcuts import render
from django.http import HttpResponse
from Familia.models import Integrantes
# Create your views here.

def papa(self):
    papa = Integrantes(nombre='Jean-Philippe', apellido= 'Ursule', nacionalidad= 'Francesa', fechaNacimiento='1982-09-13', dni='90000000')
    #papa.save()

    documento = f'El papa se llama {papa.nombre} {papa.apellido}, es de nacionalida {papa.nacionalidad} , nacio el {papa.fechaNacimiento} y tiene el numero de DNI: {papa.dni}'
    
    return HttpResponse(documento)

def mama(self):
    mama = Integrantes(nombre='Shirley', apellido= 'Vera Marquez', nacionalidad= 'Boliviana', fechaNacimiento='1985-11-07', dni='90000001')
    mama.save()
    
    documento = f'La mama se llama {mama.nombre} {mama.apellido}, es de nacionalida {mama.nacionalidad} , nacio el {mama.fechaNacimiento} y tiene el numero de DNI: {mama.dni}'
    
    return HttpResponse(documento)
    
def hija(self):
    
    hija = Integrantes(nombre='Victoria', apellido= 'Ursule Vera', nacionalidad= 'Franco-Argentina', fechaNacimiento='2019-01-23', dni='50000000')
    hija.save()
    
    documento = f'La hija se llama {hija.nombre} {hija.apellido}, es de nacionalida {hija.nacionalidad} , nacio el {hija.fechaNacimiento} y tiene el numero de DNI: {hija.dni}'
    
    return HttpResponse(documento)