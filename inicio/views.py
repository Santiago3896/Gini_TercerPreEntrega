from django.shortcuts import render, redirect
# from django.template import loader
# from django.http import HttpResponse
from inicio.models import Paleta, Cancha, Pelotitas
from inicio.forms import AlquilarPaletaFormulario , AlquilarCanchaFormulario , AlquilarPelotitasFormulario


def inicio(request):
   
    # v2
    
    # template = loader.get_template('inicio.html')
    # template_renderizado = template.render({})
    
    # return HttpResponse(template_renderizado)
    
    # v3
    
    return render(request,"inicio/inicio.html", {})

def paletas(request):
    
    listado_de_paletas = Paleta.objects.all()
    
    print(listado_de_paletas)
    
    return render(request, "inicio/estudiando_al_cliente.html", {'listado_de_paletas': listado_de_paletas})

def alquiler_exitoso(request):
    
    print("paso por aca")
    return render(request,"inicio/alquiler_exitoso.html")

def alquilar_paletas(request):
    
    if request.method == "POST":
        formulario = AlquilarPaletaFormulario(request.POST)
        if formulario.is_valid():
            info_limpiaPaletas = formulario.cleaned_data
            
            marca = info_limpiaPaletas.get("marca")
            modelo = info_limpiaPaletas.get("modelo")
            descripcion = info_limpiaPaletas.get("descripcion")
            anio = info_limpiaPaletas.get("anio")
            
            paleta = Paleta(marca = marca , modelo = modelo , descripcion = descripcion , anio = anio)
            paleta.save()
            
            return redirect(alquiler_exitoso)
        
        else:
            return render(request, "inicio/alquiler_paleta.html",{"formulario": formulario})
    
    formulario = AlquilarPaletaFormulario()
    return render(request, "inicio/alquiler_paleta.html",{"formulario" : formulario})

def alquilar_canchas(request):
    
    if request.method == "POST":
        formulario = AlquilarCanchaFormulario(request.POST)
        if formulario.is_valid():
            info_limpiaCanchas = formulario.cleaned_data
            
            numero = info_limpiaCanchas.get("numero")
            deporte = info_limpiaCanchas.get("deporte")
            tipo_piso = info_limpiaCanchas.get("tipo_piso")
            cantidad_horas = info_limpiaCanchas.get("cantidad_horas")
            
            canchas = Cancha(numero = numero , deporte = deporte , tipo_piso = tipo_piso , cantidad_horas = cantidad_horas)
            canchas.save()
            
            return redirect(alquiler_exitoso)
        
        else:
            return render(request, "inicio/alquiler_cancha.html",{"formulario": formulario})
       
    
    formulario1 = AlquilarCanchaFormulario()
    
    return render(request, "inicio/alquiler_cancha.html",{"formulario" : formulario1})

def alquilar_pelotitas(request):
    
    if request.method == "POST":
        formulario = AlquilarPelotitasFormulario(request.POST)
        if formulario.is_valid():
            info_limpiaPelotitas = formulario.cleaned_data
            
            marca = info_limpiaPelotitas.get("marca")
            deporte = info_limpiaPelotitas.get("deporte")
            cantidad = info_limpiaPelotitas.get("cantidad")
            
            pelotitas = Pelotitas(marca = marca , deporte = deporte , cantidad = cantidad)
            pelotitas.save()
            
            return redirect(alquiler_exitoso)
        
        else:
            return render(request, "inicio/alquiler_pelotitas.html",{"formulario": formulario})
    
    formulario2 = AlquilarPelotitasFormulario()
    
    return render(request, "inicio/alquiler_pelotitas.html",{"formulario" : formulario2})