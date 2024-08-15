from django import forms
from .models import Farm


class FormFarm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ['name','lat','long']
    
    def __init__(self, *args, **kwargs):
        super(FormFarm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].label = 'Nome da fazenda'
        self.fields['lat'].widget.attrs['class'] = 'form-control'
        self.fields['long'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Nome da fazenda'
        self.fields['lat'].widget.attrs['placeholder'] = 'Latitude'
        self.fields['long'].widget.attrs['placeholder'] = 'Longitude'