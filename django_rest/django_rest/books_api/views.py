from rest_framework.response import Response
from rest_framework.views import APIView

from django_rest.books_api.models import BookModel
from django_rest.books_api.serializers import BookSerializer


class BookListCreate(APIView):
    def get(self, request):
        books = BookModel.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass
