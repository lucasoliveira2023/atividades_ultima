from django import forms
from .models import ReservaBanho

class ReservaBanhoForm(forms.ModelForm):
    class Meta:
        model = ReservaBanho
        fields = ['nome_pet', 'telefone', 'dia_reserva', 'observacoes']
