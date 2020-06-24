"""FlatMX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

from branches import views
from branches.views import BranchListView

urlpatterns = [
    # Include Frontend urls
    path('', BranchListView.as_view(), name='branches-home'),
    path('', include('branches.urls')),
    path('pulls/', views.pulls, name='branches-pulls'),
    # Include API v1 urls
    path('api/v1/', include('core.urls.v1')),
    # Include Admin url
    path('admin/', admin.site.urls),
    #Documentation
    path('docs/', include_docs_urls(title='FlatMX APIRest', public=True))
]
