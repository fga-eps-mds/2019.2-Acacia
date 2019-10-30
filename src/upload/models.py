from django.db import models
from users.models import User


class Picture(models.Model):
    
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=('owner'),
        null=True,
        blank=True,
    )    
        
    owner_picture = models.ImageField(
        verbose_name=('owner picture'),
        upload_to='',
        blank=False,
        null=False,
    )
    
    def __str__(self):
        return f"{self.owner}, {self.owner_picture }"
