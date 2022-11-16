from django import forms 


class RegistroProfesorForm(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    materia = forms.CharField(max_length=40)

class RegistroTutorForm(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    materia = forms.CharField(max_length=40)

class RegistroAlumnoForm(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    materia = forms.CharField(max_length=40)

class BuscarForm(forms.Form):

    apellido = forms.CharField(max_length=40)