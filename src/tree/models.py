from django.db import models
from users.models import User
from django.utils.translation import ugettext as _

from property.models import Property

class Tree(models.Model):

    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        verbose_name=_('Property trees'),
        related_name=_('trees'),
    )

    TYPE_OF_TREES = (
        (_('Avocado'), _('Avocado')),
        (_('Pineapple'), _('Pineapple')),
        (_('Banana'), _('Banana')),
        (_('Persimmon'), _('Persimmon')),
        (_('Coconut'), _('Coconut')),
        (_('FIG'), _('FIG')),
        (_('Guava'), _('Guava')),
        (_('Jabuticaba'), _('Jabuticaba')),
        (_('Orange'), _('Orange')),
        (_('Lemon'), _('Lemon')),
        (_('Apple'), _('Apple')),
        (_('Papaya'), _('Papaya')),
        (_('Mango'), _('Mango')),
        (_('Passion Fruit'), _('Passion Fruit')),
        (_('Quince'), _('Quince')),
        (_('Nectarine'), _('Nectarine')),
        (_('Loquat'), _('Loquat')),
        (_('Pear'), _('Pear')),
        (_('Pequizeiro'), _('Pequizeiro')),
        (_('Tangerine'), _('Tangerine')),
        (_('Peach'), _('Peach')),
        (_('Vine'), _('Vine')),
    )

    tree_type = models.CharField(
       verbose_name=_('Tree of type'),
       choices=TYPE_OF_TREES,
       max_length=13,
    )

    number_of_tree = models.IntegerField(
        verbose_name=_('Number of tree'),
        default=1,
    )

    height_fruit = models.DecimalField(
        verbose_name=_('Average tree height'),
        max_digits=3,
        decimal_places=1,
    )

    def __str__(self):
        return f"{self.tree_type}, {self.number_of_tree}"


class HarvestMonth(models.Model):
    class Meta:
        verbose_name_plural = _('Harvest Months')

    tree = models.ForeignKey(
        Tree,
        models.CASCADE,
        related_name=_('harvest_months'),
    )

    MONTHS = (
            (1, _('January')),
            (2, _('February')),
            (3, _('March')),
            (4, _('April')),
            (5, _('May')),
            (6, _('June')),
            (7, _('July')),
            (8, _('August')),
            (9, _('September')),
            (10, _('October')),
            (11, _('November')),
            (12, _('December')),
        )

    harvest_month = models.IntegerField(
        choices=MONTHS,
        verbose_name=_('Harvest month'),
    )
