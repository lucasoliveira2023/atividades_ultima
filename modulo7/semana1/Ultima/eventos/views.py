from django.shortcuts import render, get_object_or_404

from eventos.models import Evento
# Create your views here.
from eventos.forms import InscricaoEventoform

def evento_detalhes(request, id):
    evento = get_object_or_404(Evento, id=id)
    form = InscricaoEventoform(request.POST or None)
    if form.is_valid():
        inscricao =form.save(commit=False)
        inscricao.evento = evento
        inscricao.save()
        sucesso = True
    else:
        sucesso = False
    contexto = {
        'evento': evento,
        'form': form,
        'sucessso': sucesso,
    }
    return render(request, 'evento.html', contexto)