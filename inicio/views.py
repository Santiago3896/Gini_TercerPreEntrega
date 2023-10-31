from django.shortcuts import render
# from django.template import loader
# from django.http import HttpResponse
from inicio.models import Paleta


def inicio(request):
   
    # v2
    
    # template = loader.get_template('inicio.html')
    # template_renderizado = template.render({})
    
    # return HttpResponse(template_renderizado)
    
    # v3
    
    return render(request,"inicio/inicio.html", {})

def paletas(request):
    paleta = Paleta(marca = "Babolat", descripcion = "Paleta de primera marca", anio = 2023)
    paleta.save()
    
    return render(request, "inicio/paletas.html", {'paleta': paleta})