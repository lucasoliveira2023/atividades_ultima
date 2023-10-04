from django.shortcuts import render
# Create your views here.
from .forms import ReservaBanhoForm

def reserva_banho(request):
    if request.method == 'POST':
        form = ReservaBanhoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'reserva/sucesso.html')
    else:
        form = ReservaBanhoForm()
    return render(request, 'reserva/reserva_banho.html', {'form': form})
