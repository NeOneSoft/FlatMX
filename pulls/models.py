# Django
from django.db import models
from django.urls import reverse

# Models
from authors.models import Author
from branches.models import Branch

STATUS = (
    ('OPEN', 'OPEN'),
    ('MERGE', 'MERGE'),
)

#PR Model
class PR(models.Model):
    merge = models.ManyToManyField(Branch, related_name='merge')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    status = models.CharField(max_length=5, choices=STATUS)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('branches-pulls')
