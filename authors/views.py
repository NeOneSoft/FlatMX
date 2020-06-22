from rest_framework import viewsets

from authors.models import Author
from authors.serializers import AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """
    Author endpoint(ViewSet)
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
