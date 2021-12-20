from rest_framework import serializers
from django_rest.books_api.models import BookModel


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = "__all__"
