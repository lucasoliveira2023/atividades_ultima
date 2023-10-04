from django.shortcuts import render

from eventos.models import Evento
# Create your views here.

def evento(request, id):
    print(id)
    contexto = {
        'evento': Evento.objects.get(id=id)
    }
    return render(request,'evento.html', contexto)