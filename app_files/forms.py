from django import forms
from .models import SourceFiles, Map


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class FormSourceFiles(forms.ModelForm):
    file = forms.FileField(label='Arquivo',widget=forms.ClearableFileInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = SourceFiles
        fields = ['title','file','map']
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(FormSourceFiles, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].label = 'Título'
        self.fields['map'].label = 'Mapa'
        self.fields['map'].widget.attrs['class'] = 'form-control'

        if user is not None:
            self.fields['map'].queryset = Map.objects.filter(user=user)