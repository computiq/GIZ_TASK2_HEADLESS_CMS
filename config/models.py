import uuid as uuid

from django.db import models

"""
As we not using database in  this task, this base model will not be used yet.
"""


class BaseModel(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False, auto_created=True, editable=False)
    uuid = models.UUIDField(default=uuid.uuid4, null=False, blank=False, auto_created=True, editable=False)
    created_at = models.DateField(auto_now_add=True, editable=False, auto_created=True)
    updated_at = models.DateField(auto_now=True, editable=False, auto_created=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
