from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title