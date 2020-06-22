# Django
from django.urls import path

# Views
from . import views
from .views import BranchListView, PullCreateView

# FRONT-END urls
urlpatterns = [
    path('', BranchListView.as_view(), name='branches-home'),
    path('commits/', views.commits, name='branches-commits'),
    path('pulls/', views.pulls, name='branches-pulls'),
    path('pulls/new/', PullCreateView.as_view(), name='pull-create'),
]