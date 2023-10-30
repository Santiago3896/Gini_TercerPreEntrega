from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def inicio(request):
   
    # v2
    
    # template = loader.get_template('inicio.html')
    # template_renderizado = template.render({})
    
    # return HttpResponse(template_renderizado)
    
    # v3
    
    return render(request,"inicio.html", {})