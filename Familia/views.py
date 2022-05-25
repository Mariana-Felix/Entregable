from django.shortcuts import render
from django.http import HttpResponse
from Familia.models import Integrantes
from django.template import loader
# Create your views here.
#Completado con los nombres y datos de los familiares
def papa(self):
    papa = Integrantes.objects.get(id=10)
    diccionario = {'papa': papa}
    template = loader.get_template('Familia/papa.html')    
    return HttpResponse(template.render(diccionario))

def mama(self):
    mama = Integrantes.objects.get(id=12)
    diccionario = {'mama': mama}
    template = loader.get_template ('Familia/mama.html')
    #mama = Integrantes(nombre='Rosa', apellido= 'Olivera', nacionalidad= 'Argentina', fechaNacimiento='1986-09-19', dni=17646352)
    #mama.save()
    
    #diccionario = {'mama': mama}
    #template = loader.get_template('Familia/mama.html')
    #documento = template.render(diccionario)
    
    return HttpResponse(template.render (diccionario))
    
def hija(self):
    hija = Integrantes.objects.get(id=13)
    diccionario = {'hija': hija}
    template = loader.get_template ('Familia/hija.html')
    #hija = Integrantes(nombre='Mariana', apellido= 'Felix', nacionalidad= 'Argentina', fechaNacimiento='1992-07-21', dni=36415093)
    #hija.save()
    
    #diccionario = {'hija': hija}
    #template = loader.get_template('Familia/hija.html')
    #documento = template.render(diccionario)
    
    return HttpResponse(template.render (diccionario))

def inicio(request):
    return render(request,'Familia/inicio.html')