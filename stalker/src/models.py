from django.db import models


class Identifier(models.Model):
    uniqueId = models.JSONField()
    createdAt = models.DateField()

    class Meta:
        ordering = ['-createdAt']
