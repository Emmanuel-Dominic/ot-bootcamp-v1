from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Business(models.Model):
    name = models.CharField(max_length=25)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='owner')
    managers = models.ManyToManyField(User, related_name='business')

    class Meta:
        verbose_name_plural = "businesses"
