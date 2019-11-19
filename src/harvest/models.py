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

    date = models.DateField()

    description = models.TextField(
        default=""
    )

    HARVEST_STATUS = (
        ('Done',        'Done'),
        ('Cancelled',   'Cancelled'),
        ('Open',        'Open'),
        ('Enough',      'Enough'),
    )

    status = models.CharField(
        choices=HARVEST_STATUS,
        max_length=9
    )

    max_volunteers = models.PositiveSmallIntegerField()
    min_volunteers = models.PositiveSmallIntegerField()

    #  TODO: check if this field will continue in this model
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

    @staticmethod
    def valid_status():
        """
        This class method returns a list of valid status
        """
        return [k for k, v in Harvest.HARVEST_STATUS]


class HarvestRules(models.Model):

    class Meta:
        verbose_name_plural = _('Harvest Rules')
        unique_together = ('harvest', 'description')

    harvest = models.ForeignKey(
        Harvest,
        models.CASCADE,
        related_name=_('rules'),
    )

    description = models.CharField(
        max_length=280,
    )

    def __str__(self):
        return self.description
