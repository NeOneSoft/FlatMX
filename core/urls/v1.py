# Django
from django.conf.urls import url, include
from rest_framework import routers
from authors.views import AuthorViewSet
from branches.views import BranchViewSet
from commits.views import CommitViewSet
from pulls.views import PRViewSet

# API urls
router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'branches', BranchViewSet)
router.register(r'commits', CommitViewSet)
router.register(r'pulls', PRViewSet)

urlpatterns = [
    url(r'', include(router.urls))
]
