from django.db import models
from django.utils import timezone
# Create your models here.
from ygdy.models import Movie
from django.contrib.auth.models import User


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.content[:20]