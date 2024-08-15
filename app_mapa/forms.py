from django import forms
from .models import Map


class FormMap(forms.ModelForm):
    class Meta:
        model = Map
        fields = ['farm','name','url','description','main_map_selected']
    
    def __init__(self, *args, **kwargs):
        super(FormMap, self).__init__(*args, **kwargs)
        self.fields['farm'].required = True
        self.fields['name'].required = True
        self.fields['description'].required = True
        self.fields['farm'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['rows'] = 3
        self.fields['description'].widget.attrs['placeholder'] = 'Descrição do mapa'
        self.fields['name'].widget.attrs['placeholder'] = 'Nome do mapa'
        self.fields['farm'].widget.attrs['placeholder'] = 'Selecione a fazenda'
        self.fields['farm'].empty_label = "Fazenda"
        self.fields['farm'].label = "Fazenda"
        self.fields['name'].label = "Nome do mapa"
        self.fields['description'].label = "Descrição do mapa"
        self.fields['url'].widget.attrs['class'] = 'form-control'
        self.fields['url'].widget.attrs['placeholder'] = 'URL do mapa'
        self.fields['url'].label = "URL do mapa"
        self.fields['main_map_selected'].widget.attrs['class'] = 'form-check-input'
        self.fields['main_map_selected'].label = "Mapa principal"
        self.fields['main_map_selected'].widget.attrs['type'] = 'checkbox'
        
        #self.fields['farm'].queryset = self.fields['farm'].queryset.filter(user=self.instance.user)