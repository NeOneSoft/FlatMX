#Django
from django.contrib import admin
#Model
from .models import Branch


@admin.register(Branch)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'branch')
    search_fields = ['branch']
    ordering = ['pk']
