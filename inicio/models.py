from django.db import models

class Paleta(models.Model):
    marca = models.CharField(max_length=10)
    modelo = models.CharField(max_length=10)
    descripcion = models.TextField()
    anio = models.IntegerField()
    
    def __str__(self):
        return f"{self.id} - {self.marca} - {self.modelo} - {self.anio}"

class Pelotitas(models.Model):
    marca = models.CharField(max_length=10)
    deporte = models.TextField()
    cantidad = models.IntegerField()
    
    def __str__(self):
        return f"{self.id} - {self.marca} - {self.deporte} - {self.cantidad}"
    
class Cancha(models.Model):
    numero = models.IntegerField()
    deporte = models.CharField( max_length=15)
    tipo_piso = models.CharField(max_length=15)
    cantidad_horas = models.FloatField()
    
    def __str__(self):
        return f"{self.id} - {self.numero} - {self.deporte} - {self.tipo_piso}"
    
    
