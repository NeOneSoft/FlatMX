#Django
from django.contrib import admin
#Model
from .models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name', 'e_mail')
    search_fields = ['first_name']
    ordering = ['pk']