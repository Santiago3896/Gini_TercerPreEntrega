from django.urls import path
from inicio.views import inicio, alquilar_paletas, alquilar_canchas, alquilar_pelotitas, alquiler_exitoso, paletas, eliminar

urlpatterns = [
    path('', inicio, name = "inicio"),
    path('paletas/alquiler', alquilar_paletas , name = "alquiler_paleta"),
    path('canchas/alquiler', alquilar_canchas , name = "alquilar_canchas"),
    path('pelotitas/alquiler', alquilar_pelotitas , name = "alquilar_pelotitas"),
    path('alquilado/correctamente', alquiler_exitoso , name = "alquiler_exitoso1"),
    path('estudiando', paletas , name = "estudiando"),
    path('eliminar/<int:paleta_id>/paleta', eliminar, name="afuera")
]