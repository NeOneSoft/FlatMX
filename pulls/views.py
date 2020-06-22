# Django
from rest_framework import viewsets

# Models and Serializers
from .models import PR
from .serializers import PRSerializer, CreatePRSerializer


class PRViewSet(viewsets.ModelViewSet):
    queryset = PR.objects.all()
    serializer_class = PRSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreatePRSerializer
        return PRSerializer
