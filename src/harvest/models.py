from django.db import models
from property.models import Property
from django.utils.translation import ugettext as _


class Harvest(models.Model):

    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        verbose_name=_('Property harvests'),
        related_name=_('harvests'),
    )

    # objects = models.Manager()

    date = models.DateField()

    description = models.TextField(
        default=""
    )

    HARVEST_STATUS = (
        ('Done', 'Done'),
        ('Cancelled', 'Cancelled'),
        ('Open', 'Open'),
        ('Enough', 'Enough'),
    )

    status = models.CharField(
        choices=HARVEST_STATUS,
        max_length=9
    )

    max_volunteers = models.PositiveSmallIntegerField()
    min_volunteers = models.PositiveSmallIntegerField()

    # probabily this field will become a new model
    # equipment = models.CharField(
    #     blank=True,
    #     null=True,
    #     max_length=2000
    # )

    # ACCESS_TYPES = (
    #     ('Restrict Access', 'Restrict Access'),
    #     ('Free Access', 'Free Access'),
    # )
    # access = models.CharField(
    #     choices=ACCESS_TYPES,
    #     max_length=15
    # )

    def __str__(self):
        return str(self.date)


class RulesHarvest(models.Model):

    harvest = models.ForeignKey(Harvest, models.CASCADE)

    description = models.CharField(
        max_length=280
    )

    def __str__(self):
        return self.description
