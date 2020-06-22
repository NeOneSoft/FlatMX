# Django
from rest_framework import serializers

# Models and Serializers
from authors.serializers import AuthorSerializer
from branches.serializers import BranchSerializer
from .models import Commit


class CommitSerializer(serializers.ModelSerializer):
    """
    Geneneral purpose Commit Serializer
    """
    author = AuthorSerializer(read_only=True)
    branches = BranchSerializer(read_only=True)

    class Meta:
        model = Commit
        fields = ('message', 'author', 'branches', 'files_changed', 'timestamp')


class CreateCommitSerializer(serializers.ModelSerializer):
    """
    Create Commit Serializer without related fields
    """

    class Meta:
        model = Commit
        fields = ('message', 'author', 'branches', 'files_changed', 'timestamp')


class ListCommitSerializer(serializers.ModelSerializer):
    """
    List Commit Serializer without related fields
    """
    author = AuthorSerializer(read_only=True)
    branches = BranchSerializer(read_only=True)

    class Meta:
        model = Commit
        fields = ('message', 'author', 'timestamp', 'branches')
