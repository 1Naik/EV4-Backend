from django import forms
from .models import Reserva

class ReservaRegistroForms(forms.Form):

    ESTADOS = [
        ('RESERVADO','Reservado'),
        ('COMPLETADA','Completada'),
        ('ANULADA','Anulada'),
        ('NO ASISTEN','No asisten'),
    ]

    nombre = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    telefono = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    fecha_reserva = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'class':'form-control', 'type':'time'}))
    cantidad_personas = forms.IntegerField(min_value=1, max_value=15, widget=forms.NumberInput(attrs={'class':'form-control'}))
    estado = forms.ChoiceField(choices=ESTADOS, widget=forms.Select(attrs={'class':'form-control'}))
    observacion = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control'}))


class ReservaRegistroForms(forms.ModelForm):

    ESTADOS = [
        ('RESERVADO','Reservado'),
        ('COMPLETADA','Completada'),
        ('ANULADA','Anulada'),
        ('NO ASISTEN','No asisten'),
    ]

    nombre = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    telefono = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    fecha_reserva = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'class':'form-control', 'type':'time'}))
    cantidad_personas = forms.IntegerField(min_value=1, max_value=15, widget=forms.NumberInput(attrs={'class':'form-control'}))
    estado = forms.ChoiceField(choices=ESTADOS, widget=forms.Select(attrs={'class':'form-control'}))
    observacion = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control'}))

    class Meta:
        model = Reserva
        fields = '__all__'