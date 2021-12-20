from django import forms

from pythons_app.models import Python


class PythonCreateForm(forms.ModelForm):
    class Meta:
        model = Python
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'image': forms.FileInput(attrs={'class': 'custom-file-input'}),
        }
        fields = '__all__'
