from django.shortcuts import render
from .models import ProfesoresCoder, TutoresCoder, AlumnosCoder
from .forms import RegistroAlumnoForm, RegistroProfesorForm, RegistroTutorForm, BuscarForm




def vista_inicio(request):

    return render (request, "index.html")
# Create your views here.

def vista_referencias(request):

    return render (request, "referencias.html")



def registro_profesores(request):

    if request.method == 'POST':

        formregistroprofe = RegistroProfesorForm(request.POST)

        if formregistroprofe.is_valid():

            formu_limpio = formregistroprofe.cleaned_data

            profe = ProfesoresCoder(nombre = formu_limpio["nombre"], apellido = formu_limpio["apellido"], edad = formu_limpio["edad"], materia = formu_limpio["materia"])

            profe.save()

            return render (request, "RegistroExitoso.html")
    else:

        formregistroprofe = RegistroAlumnoForm()

    return render (request, "Registro_Profesores.html", {"formulario" : formregistroprofe})






def registro_tutores(request):

    if request.method == 'POST':

        formregistrotutor = RegistroTutorForm(request.POST)

        if formregistrotutor.is_valid():

            formu_limpio = formregistrotutor.cleaned_data

            tutor = TutoresCoder(nombre = formu_limpio["nombre"], apellido = formu_limpio["apellido"], edad = formu_limpio["edad"], materia = formu_limpio["materia"])

            tutor.save()

            return render (request, "RegistroExitoso.html")
    else:

        formregistrotutor = RegistroTutorForm()

    return render (request, "Registro_Tutores.html", {"formulario" : formregistrotutor})





def registro_alumnos(request):

    if request.method == 'POST':

        formregistroalumno = RegistroAlumnoForm(request.POST)

        if formregistroalumno.is_valid():

            formu_limpio = formregistroalumno.cleaned_data

            alumno = AlumnosCoder(nombre = formu_limpio["nombre"], apellido = formu_limpio["apellido"], edad = formu_limpio["edad"], materia = formu_limpio["materia"])

            alumno.save()

            return render (request, "RegistroExitoso.html")
    else:

        formregistroalumno = RegistroAlumnoForm()

    return render (request, "Registro_Alumnos.html", {"formulario" : formregistroalumno})


def busqueda_profesores(request):

    if request.GET.get("apellido", False):

        apellido = request.GET["apellido"]
        profesor = ProfesoresCoder.objects.filter(apellido=apellido)

        return render (request, "Busqueda_Profesores.html", {"profesor": profesor})
        
    else:

        respuesta = "No hay datos que coincidan"
        
    return render (request, "Busqueda_Profesores.html", {"respuesta": respuesta})

    

def busqueda_tutores(request):

    if request.GET.get("apellido", False):

        apellido = request.GET["apellido"]
        tutor = TutoresCoder.objects.filter(apellido=apellido)

        return render (request, "Busqueda_Tutores.html", {"tutor": tutor})
        
    else:

        respuesta = "No hay datos que coincidan"
        
    return render (request, "Busqueda_Tutores.html", {"respuesta": respuesta}) 




def busqueda_alumnos(request):

    if request.GET.get("apellido", False):

        apellido = request.GET["apellido"]
        alumno = AlumnosCoder.objects.filter(apellido=apellido)

        return render (request, "Busqueda_Alumnos.html", {"alumno": alumno})
        
    else:

        respuesta = "No hay datos que coincidan"
        
    return render (request, "Busqueda_Alumnos.html", {"respuesta": respuesta}) 
