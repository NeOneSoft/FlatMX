from django.db import models


# Author model
class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    e_mail = models.EmailField()

    def __str__(self):
        """Return first_name and last_name"""
        return '{} {}'.format(self.first_name, self.last_name)
