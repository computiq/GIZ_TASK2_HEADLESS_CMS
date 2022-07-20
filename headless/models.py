from ckeditor.fields import RichTextField
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    content = RichTextField(null=False, blank=False)

    def __str__(self):
        return self.title
