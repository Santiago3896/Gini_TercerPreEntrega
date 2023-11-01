from django.urls import path
from inicio.views import inicio, paletas , alquilar_paletas, alquilar_canchas, alquilar_pelotitas

urlpatterns = [
    path('', inicio, name = "inicio"),
    path('paletas/', paletas, name = "paletas"),
    path('paletas/alquilar', alquilar_paletas , name = "alquilar_paleta"),
    path('canchas/alquilar', alquilar_canchas , name = "alquilar_paleta"),
    path('pelotitas/alquilar', alquilar_pelotitas , name = "alquilar_paleta")  
]