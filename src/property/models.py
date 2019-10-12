from django.db import models
from django.utils.translation import ugettext as _
from localflavor.br.br_states import STATE_CHOICES

from users.models import User

class Property(models.Model):

    class Meta:
        unique_together = ('BRZipCode', 'type_of_address', 'address')
        verbose_name_plural = _('Properties')

    TYPE_OF_ADDRESS = (
        (_('Apartment'), _('Apartment')),
        (_('House'),     _('House')),
        (_('Farm'),      _('Farm')),
        (_('Other'),     _('Other')),
    )

    type_of_address = models.CharField(
        choices = TYPE_OF_ADDRESS,
        max_length = 9,
        verbose_name = _('Type of address'),
        null = False,
        blank = False,
    )

    BRZipCode = models.CharField(
        max_length = 8,
        verbose_name = _('Brazilian ZIP code'),
        null = False,
        blank = False,
    )

    state = models.CharField(
        max_length = 2,
        choices = STATE_CHOICES,
        null = False,
        blank = False
    )

    city = models.CharField(
        max_length = 100,
        verbose_name = _('City'),
        null = False,
        blank = False,
    )

    district = models.CharField(
        max_length = 100,
        verbose_name = _('District'),
        null = False,
        blank = False,
    )

    address = models.CharField(
        max_length = 100,
        verbose_name = _('Address'),
        null = False,
        blank = False,
    )

    complement = models.CharField(
        max_length = 100,
        verbose_name = _('Address complement')
    )

    reference_point = models.CharField(
        max_length = 100,
        verbose_name = _('Reference point'),
    )

    owner = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        verbose_name = _('Property owner'),
        related_name = _('properties'),
        null = False,
        blank = False,
    )

    def __str__(self):
        return f"{self.state}, {self.city}, {self.address}"