import uuid
from django.db import models

# Create your models here.
class Entity(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField( primary_key = True,default=uuid.uuid4(),editable=False)
    created = models.DateTimeField(editable=False,auto_now_add=True)
    updated = models.DateTimeField(editable=False,auto_now=True)



class Posts(models.Model):
    title = models.CharField('title', max_length =300)
    description = models.TextField('description', null=True , blank=True)



