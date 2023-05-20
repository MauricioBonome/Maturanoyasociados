from django import forms

class VentaForm(forms.Form):
    nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    telefono = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    localidad = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    provincia = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    comentarios = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    aceptar_terminos = forms.BooleanField(required=True)

    def __init__(self, *args, **kwargs):
        super(VentaForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].label = 'Nombre'
        self.fields['email'].label = 'Email'
        self.fields['telefono'].label = 'Teléfono'
        self.fields['localidad'].label = 'Localidad'
        self.fields['provincia'].label = 'Provincia'
        self.fields['comentarios'].label = 'Comentarios'
        self.fields['aceptar_terminos'].label = 'Acepto los Términos y Condiciones de Uso y la Política de Privacidad'
