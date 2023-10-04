from django.shortcuts import render

# Create your views here.
from .forms import ReservaForm

def reservar_banho(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'reserva_pet/sucesso_reserva.html')
    else:
        form = ReservaForm()
    return render(request, 'reserva_pet/reserva_form.html', {'form': form})
