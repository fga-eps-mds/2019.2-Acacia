from django.db import models

# Create your models here.

class Harvest(models.Model):

    objects = models.Manager()

    date = models.DateField(
        null=True
    )

    rules = models.CharField(
        blank=True,
        null=False,
        default="",
        max_length=2000 
    )

    description = models.TextField(
        blank=True,
        null=True,
        default=""
    )

    status = models.CharField(
        blank=True,
        null=False,
        default="",
        max_length=280
    )

    max_volunteers = models.PositiveSmallIntegerField(
        blank=True,
        null=False,
    )

    neighbor_access = models.BooleanField(
        default=False,
        blank=True, 
        null=False
    )

    equipament = models.CharField(
        blank=True,
        null=False,
        default="",
        max_length=2000 
    )