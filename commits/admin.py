#Django
from django.contrib import admin
#Model
from .models import Commit


@admin.register(Commit)
class CommitAdmin(admin.ModelAdmin):
    list_display = ('pk', 'message', 'author', 'branches', 'files_changed', 'timestamp')
    search_fields = ['branches']
    ordering = ['pk']
