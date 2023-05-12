from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    link=models.URLField()
    thumbnail=models.ImageField()
    slug = models.SlugField(default="", null=False, unique=True)
    views = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.title
