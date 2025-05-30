from django import forms
from .models import ChamadoModel

class ChamadoForm(forms.ModelForm):
    class Meta:
        model = ChamadoModel  
        fields = ['empresa', 'especialidades', 'descricao', 'localizacao'] 
        widgets = {
            'empresa': forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'Nome da Empresa'}),
            'especialidades': forms.Textarea(attrs={'class': 'form__input', 'rows': 3, 'placeholder': 'Especialidades'}),
            'descricao': forms.Textarea(attrs={'class': 'form__input', 'placeholder': 'Descrição do Chamado'}),
            'localizacao': forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'Localização'}),
        }