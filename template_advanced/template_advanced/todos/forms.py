from django import forms

from template_advanced.todos.models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
