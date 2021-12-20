from django.urls import path

from Retake_exam_app.books.views import index, add_book, details_book, edit_book, delete_book

urlpatterns = (
    path('', index, name='index'),
    path('add/', add_book, name='add book'),
    path('details/<int:pk>', details_book, name='details book'),
    path('edit/<int:pk>', edit_book, name='edit book'),
    path('delete/<int:pk>', delete_book, name='delete book'),
)
