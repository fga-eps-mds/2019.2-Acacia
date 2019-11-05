from django.db import models


class Harvest(models.Model):

    # TODO A Harvest belongs to a property

    def __str__(self):
        return str(self.date)

    objects = models.Manager()

    date = models.DateField()

    description = models.TextField(
        blank=True,
        null=True,
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
    equipment = models.CharField(
        blank=True,
        null=True,
        max_length=2000
    )

    # ACCESS_TYPES = (
    #     ('Restrict Access', 'Restrict Access'),
    #     ('Free Access', 'Free Access'),
    # )
    # access = models.CharField(
    #     choices=ACCESS_TYPES,
    #     max_length=15
    # )


class RulesHarvest(models.Model):

    def __str__(self):
        return self.description

    harvest = models.ForeignKey(Harvest, models.CASCADE)

    description = models.CharField(
        max_length=280
    )
