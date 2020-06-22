from rest_framework import serializers
from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    """
    Geneneral purpose Author Serializer
    """

    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'e_mail')