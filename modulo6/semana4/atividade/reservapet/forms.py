from django import forms
from django.core.exceptions import ValidationError
from .models import ReservaBanho

class ReservaBanhoForm(forms.ModelForm):
    class Meta:
        model = ReservaBanho
        fields = ['nome_pet', 'telefone', 'dia_reserva', 'observacoes']

    def clean(self):
        cleaned_data = super().clean()
        dia_reserva = cleaned_data.get('dia_reserva')

        if dia_reserva:
            # Verifique se já existem 4 reservas para o mesmo dia
            mesmo_dia = ReservaBanho.objects.filter(dia_reserva=dia_reserva).count()

            if mesmo_dia >= 4:
                raise ValidationError('Já ha 4 reservas para este dia. Por favor, escolha outro dia.')

        return cleaned_data
