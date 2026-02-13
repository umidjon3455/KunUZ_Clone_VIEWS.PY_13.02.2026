from django.db import models
from django.utils import timezone

# Category modeli
class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class News(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        Published = 'PB', 'Published'

    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT
    )

#    objects = models.Manager()

    class Meta:
        ordering = ["-publish_time"]

    def __str__(self):
        return self.title
