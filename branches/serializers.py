from rest_framework import serializers
from .models import Branch


class BranchSerializer(serializers.ModelSerializer):
    """
    Geneneral purpose Branch Serializer
    """

    class Meta:
        model = Branch
        fields = ('id', 'branch')
