from django import forms 


class InscreverForm(forms.Form):
    
    nome = forms.CharField(label='Nome')
    email= forms.EmailField(label='E-mail')
    observacoes = forms.CharField(label='observacoes', widget=forms.Textarea)
    data = forms.CharField(label='Data', required=False)