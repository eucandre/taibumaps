from django import forms
from .models import SourceFiles


class FormSourceFiles(forms.ModelForm):
    file = forms.FileField(label='Arquivo(s)',widget=forms.ClearableFileInput(attrs={'multiple': True, 'class':'form-control'}))
    class Meta:
        model = SourceFiles
        fields = ['title','file']
    
    def __init__(self, *args, **kwargs):
        super(FormSourceFiles, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].label = 'Título'
        