# Django imports
from django.db import models
from django.core.validators import MinValueValidator

# Model imports

from authors.models import Author
from branches.models import Branch


class Commit(models.Model):
    message = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    branches = models.ForeignKey(Branch, on_delete=models.CASCADE)
    files_changed = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
