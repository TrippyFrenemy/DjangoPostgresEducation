from django.db import models

# Create your models here.
class Author(models.Model):
    fullname = models.CharField(max_length=100)
    born_date = models.CharField(max_length=50)
    born_location = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.fullname


class Quote(models.Model):
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    quote = models.TextField()
    tags = models.JSONField()

    def __str__(self):
        return f"Quote by {self.author.fullname}"
