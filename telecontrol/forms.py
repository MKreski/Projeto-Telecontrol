from django import forms
from .models import ChamadoModel

class ChamadoForm(forms.ModelForm):
    class Meta:
        model = ChamadoModel  
        fields = ['empresa', 'especialidades', 'localizacao'] 
        widgets = {
            'empresa': forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'Nome da Empresa'}),
            'especialidades': forms.Textarea(attrs={'class': 'form__input', 'rows': 3, 'placeholder': 'Especialidades'}),
            'localizacao': forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'Localização'}),
        }

OPCOES = [
    ('a', 'Opção A'),
    ('b', 'Opção B'),
    ('c', 'Opção C'),
    ('d', 'Opção D'),
]

class FormularioComLimite(forms.Form):
    escolhas = forms.MultipleChoiceField(
        choices=OPCOES,
        widget=forms.CheckboxSelectMultiple,
        label="Escolha suas opções"
    )

# utils.py ou forms.py (caso queira direto lá)
def ler_opcoes_txt(caminho='BackEnd\arquivos\areas_tecnicas_conserto.txt'):
    with open(caminho, encoding='utf-8') as f:
        return [(linha.strip(), linha.strip()) for linha in f if linha.strip()]

class MeuFormulario(forms.Form):
    fruta = forms.ChoiceField(
        label="Escolha uma fruta",
        choices=ler_opcoes_txt(),  # Lê direto do txt
    )
