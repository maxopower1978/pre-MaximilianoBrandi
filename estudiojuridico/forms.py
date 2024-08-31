from django import forms
from .models import Cliente, Asesoramiento, Cita

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"

class AsesoramientoForm(forms.ModelForm):
    class Meta:
        model = Asesoramiento
        fields = "__all__"

class CitaForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), empty_label="Seleccione Cliente")
    derecho = forms.ModelChoiceField(
        queryset = Asesoramiento.objects.filter(disponible = True), empty_label="Seleccione Derecho"
        )
    class Meta:
        model = Cita
        fields = "__all__"
        widgets = {"fecha_cita": forms.DateInput(attrs={"type": "date"}), "hora": forms.TimeInput(attrs={"type": "time"})}
