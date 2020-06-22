# Django
import requests
from rest_framework import viewsets, status
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView


# Models and Serializers
from .models import Branch
from .serializers import BranchSerializer
from commits.models import Commit
from commits.serializers import ListCommitSerializer
from pulls.models import PR

# Decorators
from rest_framework.decorators import action
from rest_framework.response import Response


def home(request):
    context = {
        'branches': Branch.objects.all()
    }
    return render(request, 'branches/home.html', context)


class BranchListView(ListView):
    model = Branch
    template_name = 'branches/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'branches'
    ordering = ['-branch']
    paginate_by = 5


class BranchDetailView(DetailView):
    model = Branch


def commits(request):
    response = requests.get('http://127.0.0.1:8000/api/v1/commits')
    commits = response.json()
    return render(request, 'branches/commits.html', {"data": commits})


def pulls(request):
    response = requests.get('http://127.0.0.1:8000/api/v1/pulls')
    pulls = response.json()
    return render(request, 'branches/pulls.html', {"data": pulls})


class PullCreateView(CreateView):
    model = PR
    fields = ['merge', 'author', 'title', 'description', 'status']


class BranchViewSet(viewsets.ModelViewSet):
    """
    Branch endpoint(ViewSet)
    """
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

    @action(detail=True, methods=['GET'])
    def commits(self, request, pk=None):
        branch = self.get_object()
        commits = Commit.objects.filter(branches__id=branch.id)
        serialized = ListCommitSerializer(commits, many=True)
        if not commits:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'This branches has not commits'})
        return Response(status=status.HTTP_200_OK, data=serialized.data)
