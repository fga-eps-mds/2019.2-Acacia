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
        choices=TYPE_OF_ADDRESS,
        max_length=9,
        verbose_name=_('Type of address'),
    )

    BRZipCode = models.CharField(
        max_length=8,
        verbose_name=_('Brazilian ZIP code'),
    )

    state = models.CharField(
        max_length=2,
        choices=STATE_CHOICES,
    )

    city = models.CharField(
        max_length=100,
        verbose_name=_('City'),
    )

    district = models.CharField(
        max_length=100,
        verbose_name=_('District'),
    )

    address = models.CharField(
        max_length=100,
        verbose_name=_('Address'),
    )

    complement = models.CharField(
        max_length=100,
        verbose_name=_('Address complement'),
        default=""
    )

    reference_point = models.CharField(
        max_length=100,
        verbose_name=_('Reference point'),
        default=""
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('Property owner'),
        related_name=_('properties'),
    )

    def __str__(self):
        return f"{self.state}, {self.city}, {self.address}"

    @staticmethod
    def valid_address():
        """
        This class method returns a list of valid address
        types
        """
        return [k for k, v in Property.TYPE_OF_ADDRESS]

    @staticmethod
    def valid_states():
        """
        This class method returns a list of valid states
        """
        return [k for k, v in STATE_CHOICES]
