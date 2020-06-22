# Django
from rest_framework import viewsets

# Models and Serializers
from commits.models import Commit
from commits.serializers import CommitSerializer, CreateCommitSerializer


class CommitViewSet(viewsets.ModelViewSet):
    """
    Commit endpoint(ViewSet)
    """
    queryset = Commit.objects.all()
    serializer_class = CommitSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateCommitSerializer
        return CommitSerializer
