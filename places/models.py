from django.contrib.gis.db import models
import uuid
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

class Collection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=256, blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return str(self.id)


class Feature(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    collection = models.ForeignKey('Collection', models.CASCADE, related_name='features')
    name = models.CharField(max_length=512, blank=True, null=True)
    properties = JSONField(default={})
    geometry = models.GeometryField(blank=True, null=True)    

    def __str__(self):
        return str(self.id)