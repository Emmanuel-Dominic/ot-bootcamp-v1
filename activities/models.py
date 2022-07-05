from django.db import models
from django.conf import settings


# Create your models here.
class Activity(models.Model):
    name = models.CharField(max_length=25)
    business = models.ForeignKey('businesses.Business', on_delete=models.CASCADE)
    managers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='activity')

    class Meta:
        verbose_name_plural = "activities"
