from django.db import models

from config.models import BaseModel


class Post(BaseModel):
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.title
