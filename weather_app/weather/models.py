from django.db import models
from django.contrib.postgres.fields import JSONField


class City(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    data = JSONField(default=dict)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name: 'City'
        verbose_name_plural: 'Cities'


