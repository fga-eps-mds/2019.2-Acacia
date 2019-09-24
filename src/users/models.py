from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):

    email = models.EmailField(_('email address'), blank=False, unique=True)

    phone_number = PhoneNumberField(blank=True) # TODO: Unique Phone Number

    bio = models.TextField(blank=True)

    birth = models.DateField(blank=True, null=True)

    speaks_french = models.BooleanField(
        _('speaks french'),
        default=False,
        help_text=_('Designates If the user speaks French.'),
    )

    speaks_english = models.BooleanField(
        _('speaks english'),
        default=False,
        help_text=_('Designates If the user speaks English.'),
    )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']