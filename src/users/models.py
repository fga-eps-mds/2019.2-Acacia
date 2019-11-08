from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):

    email = models.EmailField(
        _('email address'),
        unique=True,
        blank=False,
        error_messages={
            'unique': 'A user with that email already exists.',
        }
    )
    phone_number = PhoneNumberField(
        blank=True,
        null=True
    )

    bio = models.TextField(
        blank=True,
        null=True
    )

    birth = models.DateField(
        blank=True,
        null=True
    )

    is_verified = models.BooleanField(
        'verified',
        default=True,
        help_text=(
            'Set to true when the user have verified its email address.'
        )
    )

    chosen_language = models.CharField(
       _('language'),
       max_length=2,
       default='pt',
       help_text=_('User selected language for website display')
    )

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


class Profile(models.Model):

    objects = models.Manager()

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    phone_number = models.CharField(
        blank=True,
        null=False,
        default="",
        max_length=15
    )

    bio = models.TextField(
        blank=True,
        null=False,
        default=""
    )

    birthdate = models.DateField(
        null=True,
    )

    photo = models.ImageField(
        upload_to='media/profile_photo',
        blank=True,
        null=True
    )

    is_owner = models.BooleanField(
        default=False,
        help_text=_('Designates if user has a propriety'),
        blank=True,
        null=False
    )

    is_volunteer = models.BooleanField(
        default=False,
        help_text=_('Designates if user is a volunteer'),
        blank=True,
        null=False
    )

    is_leader = models.BooleanField(
        default=False,
        help_text=_('Designates if user is a haverst leader'),
        blank=True,
        null=False
    )
