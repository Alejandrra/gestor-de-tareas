#formulario de registro

# tareas/forms.py
from django import forms
from django.contrib.auth.models import User

class RegistroUsuarioForm(forms.ModelForm):
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if password != password_confirm:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return password_confirm
