from django.db import models
from users.models import User

#from property.models import Property

class Tree(models.Model):
    class Meta:
        verbose_name_plural = ('Trees')
    
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=('Tree owner'),
        related_name=('Tree'),
        null=False,
        blank=False,
    )
    
    tree_type = models.CharField(
       verbose_name=('Tree of type'),
       max_length=30,
       null=False,
        blank=False,
    )
    
    number_of_tree = models.IntegerField(
        verbose_name=('Number of tree'),
        default=1,
        null=False,
        blank=False,
    )
    
    height_fruit = models.DecimalField(
        verbose_name=('Average height of fruits '),
        max_digits=3,
        decimal_places=2,
        null=False,
        blank=True,
    )
    
    matury_date = models.DateField(
        verbose_name=('Matury date '),
        null=False,
        blank=True,
    )
    
    haverst_for_year = models.IntegerField(
        verbose_name=('Haverst for Year'),
        null=True,
        blank=True,
    )
  
    tree_picture = models.ImageField(
        verbose_name=('Tree Picture'),
        upload_to='tree',
        blank=True,
        null=True,
    )

    # property = Models.ForeignKey( 
    #     Property,
    #     on_delete=models.CASCADE,
    #     verbose_name=_('Tree property'),
    #     related_name=_('trees'),
    #     null=False,
    #     blank=False,
    # )
    
    def __str__(self):
        return f"{self.tree_type}, {self.number_of_tree }, {self.matury_date}"
