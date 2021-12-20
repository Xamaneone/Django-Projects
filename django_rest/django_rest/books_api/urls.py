from django.urls import path

from django_rest.books_api.views import BookListCreate

urlpatterns = (
    path('', BookListCreate.as_view()),
)
