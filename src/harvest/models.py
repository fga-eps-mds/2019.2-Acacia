from django.db import models

# Create your models here.

class Harvest(models.Model):

    # TODO A Harvest belongs to a property

    def __str__ (self):
        return str(self.date)

    objects = models.Manager()

    date = models.DateField(
        null=True
    )

    description = models.TextField(
        blank=True,
        null=True,
        default=""
    )

    status = models.CharField(
        blank=True,
        null=True,
        default="",
        max_length=280
    )

    max_volunteers = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
    )

    equipment = models.CharField(
        blank=True,
        null=True,
        default="",
        max_length=2000 
    )

    neighbor_access = models.BooleanField(
        default=False,
        blank=True, 
        null=True
    )

class RulesHarvest(models.Model):

    def __str__ (self):
        return self.description

    harvest = models.ForeignKey(Harvest, models.CASCADE)

    description = models.CharField(
        blank=True,
        null=False,
        default="",
        max_length=280 
    )
