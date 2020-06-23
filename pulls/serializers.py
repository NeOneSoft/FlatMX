# Django
from rest_framework import serializers

# Models and Serializers
from authors.serializers import AuthorSerializer
from .models import PR


class PRSerializer(serializers.ModelSerializer):
    """
    General pupose
    """
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = PR
        fields = ('id', 'merge', 'author', 'title', 'description', 'status')


class CreatePRSerializer(serializers.ModelSerializer):
    """
    Create serializar
    """

    class Meta:
        model = PR
        fields = ('merge', 'author', 'title', 'description', 'status')
