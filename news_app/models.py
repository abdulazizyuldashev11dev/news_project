from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=150)


    def __str__(self):
        return self.name

class News(models.Model):
    class Status(models.TextChoices):
        Draft = "DF", "Draft",
        Published = "PB", "Published"

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.Draft)

    class Meta:
        ordering = ["-published_date"]

    def __str__(self):
        return self.title

