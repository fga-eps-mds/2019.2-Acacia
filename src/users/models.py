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
    print(instance, "Taok")
    Profile.objects.create(user=instance)

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    phone_number = PhoneNumberField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='media/profile_photo')
    is_owner = models.BooleanField(
        default=False,
        help_text=_('Designates if user has a propriety')
    )
    is_volunteer = models.BooleanField(
        default=False,
        help_text=_('Designates if user is a volunteer')
    )
    is_leader = models.BooleanField(
        default=False,
        help_text=_('Designates if user is haverst leader')
    )
