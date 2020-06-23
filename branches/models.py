from django.db import models


# Branch Model
class Branch(models.Model):
    branch = models.CharField(max_length=200)

    def __str__(self):
        return self.branch

