from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):

    email = models.EmailField(
        _('email address'),
        unique=True,
        blank=False,
        error_messages={
            'unique': 'A user with that email already exists.',
        }
    )

    is_verified = models.BooleanField(
        'verified',
        default=True,
        help_text=(
            'Set to true when the user have verified its email address.'
        )
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

@receiver(post_save, sender=User)
def create_profile(sender, instance, **kwargs):
    Profile.objects.create(user=instance)

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    phone_number = models.CharField(blank=True, null=True, max_length=15)
    bio = models.TextField(blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='media/profile_photo', blank=True, null=True)
    is_owner = models.BooleanField(
        default=False,
        help_text=_('Designates if user has a propriety'),
        blank=True, 
        null=True
    )
    is_volunteer = models.BooleanField(
        default=False,
        help_text=_('Designates if user is a volunteer'),
        blank=True, 
        null=True
    )
    is_leader = models.BooleanField(
        default=False,
        help_text=_('Designates if user is a haverst leader'),
        blank=True, 
        null=True
    )
