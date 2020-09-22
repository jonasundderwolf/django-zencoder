from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from django_zencoder.models import Format


class Video(models.Model):
    video_file = models.FileField()

    formats = GenericRelation(Format)

    class Meta:
        app_label = "example"
