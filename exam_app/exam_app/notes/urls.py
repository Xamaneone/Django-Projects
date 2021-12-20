from django.urls import path

from exam_app.notes.views import index, create_note, details_note, edit_note, delete_note

urlpatterns = [
    path('', index, name='index'),
    path('add/', create_note, name='create note'),
    path('details/<int:pk>', details_note, name='details note'),
    path('edit/<int:pk>', edit_note, name='edit note'),
    path('delete/<int:pk>', delete_note, name='delete note'),
]
