#Django
from django.contrib import admin
#Model
from .models import PR


@admin.register(PR)
class PRAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'title', 'description', 'status')
    search_fields = ['author']
    ordering = ['pk']
