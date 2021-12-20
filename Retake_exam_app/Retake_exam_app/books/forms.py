from django import forms

from Retake_exam_app.books.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'description': forms.TextInput(attrs={'placeholder': 'Description'}),
            'image': forms.TextInput(attrs={'placeholder': 'Image'}),
            'type': forms.TextInput(attrs={'placeholder': 'Fiction, Novel, Crime...'}),
        }
        labels = {
            'title': 'Title',
            'description': 'Description',
            'image': 'Image',
            'type': 'Type',
        }



class DeleteBookForm(BookForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled'] = 'disabled'
