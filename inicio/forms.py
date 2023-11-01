from django import forms

class AlquilarPaletaFormulario(forms.Form):
    marca = forms.CharField(max_length=10)
    modelo = forms.CharField(max_length=10)
    descripcion = forms.CharField(max_length=10)
    anio = forms.IntegerField()

class AlquilarCanchaFormulario(forms.Form):
    numero = forms.IntegerField()
    deporte = forms.CharField( max_length=15)
    tipo_piso = forms.CharField(max_length=15)
    cantidad_horas = forms.FloatField()

class AlquilarPelotitasFormulario(forms.Form):
    marca = forms.CharField(max_length=10)
    deporte = forms.CharField(max_length=10)
    cantidad = forms.IntegerField()