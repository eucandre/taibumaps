from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'name','role')
    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['autofocus'] = True
        self.fields['email'].label = 'E-mail'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['name'].label = 'Nome'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['role'].label = 'Perfil de Acesso'
        self.fields['role'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].label = 'Senha'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].label = 'Confirmação da Senha'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'name','role')
