from django.urls import path
from inicio.views import inicio, alquilar_paletas, alquilar_canchas, alquilar_pelotitas

urlpatterns = [
    path('', inicio, name = "inicio"),
    path('paletas/alquiler', alquilar_paletas , name = "alquiler_paleta"),
    path('canchas/alquiler', alquilar_canchas , name = "alquilar_canchas"),
    path('pelotitas/alquiler', alquilar_pelotitas , name = "alquilar_pelotitas")  
]