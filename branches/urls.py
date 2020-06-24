# Django
from django.urls import path

# Views
from pulls.views import pull_update
from . import views
from .views import BranchListView, PullCreateView, BranchDetailView

# Frontend urls
urlpatterns = [
    path('', BranchListView.as_view(), name='branches-home'),
    path('branch/<int:pk>/', BranchDetailView.as_view(), name='branches-detail'),
    path('commits/', views.commits, name='branches-commits'),
    path('pulls/', views.pulls, name='branches-pulls'),
    path('pulls/new/', PullCreateView.as_view(), name='pull-create'),
    path('pull/<int:pk>/update', pull_update, name='pull-status'),
]
