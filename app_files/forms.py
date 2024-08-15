from django import forms
from .models import SourceFiles


class FormSourceFiles(forms.ModelForm):
    class Meta:
        model = SourceFiles
        fields = ['title','file']
    
    def __init__(self, *args, **kwargs):
        super(FormSourceFiles, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['file'].widget.attrs['class'] = 'form-control'
        self.fields['file'].label = 'Arquivo(s)'
        self.fields['title'].label = 'Título'
        self.fields['file'].widget.attrs['multiple'] = True