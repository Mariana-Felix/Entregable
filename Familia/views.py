from django.shortcuts import render
from django.http import HttpResponse
from Familia.models import Integrantes
from django.template import loader
# Create your views here.

def papa(self):
    papa = Integrantes(nombre='Jean-Philippe', apellido= 'Ursule', nacionalidad= 'Francesa', fechaNacimiento='1982-09-13', dni='90000000')
    #papa.save()
    diccionario = {'papa': papa}
    template = loader.get_template('papa.html')
    documento = template.render(diccionario)
    
    
    return HttpResponse(documento)

def mama(self):
    mama = Integrantes(nombre='Shirley', apellido= 'Vera Marquez', nacionalidad= 'Boliviana', fechaNacimiento='1985-11-07', dni='90000001')
    #mama.save()
    
    diccionario = {'mama': mama}
    template = loader.get_template('mama.html')
    documento = template.render(diccionario)
    
    return HttpResponse(documento)
    
def hija(self):
    
    hija = Integrantes(nombre='Victoria', apellido= 'Ursule Vera', nacionalidad= 'Franco-Argentina', fechaNacimiento='2019-01-23', dni='50000000')
    #hija.save()
    
    diccionario = {'hija': hija}
    template = loader.get_template('hija.html')
    documento = template.render(diccionario)
    
    return HttpResponse(documento)