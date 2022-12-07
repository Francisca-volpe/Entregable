from django.shortcuts import render
from .models import *
import datetime

def familia (request):
    padre=Familiares(nombre="Andres", apellido="Volpe", parentezco="padre", edad=58)
    madre=Familiares(nombre="Teresa", apellido="Borche", parentezco="madre", edad=49)
    hermano=Familiares(nombre="Juan", apellido="Volpe", parentezco="hermano", edad=18)

    padre.save()
    madre.save()
    hermano.save()

    return render(request,"EntregableApp/template1.html", {"padre":padre, "madre":madre, "hermano":hermano})
