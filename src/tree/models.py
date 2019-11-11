from django.db import models
from django.utils.translation import ugettext as _
from property.models import Property


class Tree(models.Model):

    class Meta:
        unique_together = ('property', 'tree_type')

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

    tree_height = models.DecimalField(
        verbose_name=_('Average tree height'),
        decimal_places=1,
        max_digits=3,
    )

    picture = models.ImageField(upload_to='static/trees', blank=True,
                                null=True)

    def __str__(self):
        return (f"{self.pk}, " +
                f"{self.tree_type}, " +
                f"{self.number_of_tree}")

    @staticmethod
    def valid_tree_types():
        """
        This class method returns a list of valid address
        types
        """
        return [k for k, v in Tree.TYPE_OF_TREES]


class HarvestMonth(models.Model):
    class Meta:
        verbose_name_plural = _('Harvest Months')
        unique_together = ('tree', 'harvest_month')

    tree = models.ForeignKey(
        Tree,
        models.CASCADE,
        related_name=_('harvest_months'),
    )

    MONTHS = (
            (_('January'), _('January')),
            (_('February'), _('February')),
            (_('March'), _('March')),
            (_('April'), _('April')),
            (_('May'), _('May')),
            (_('June'), _('June')),
            (_('July'), _('July')),
            (_('August'), _('August')),
            (_('September'), _('September')),
            (_('October'), _('October')),
            (_('November'), _('November')),
            (_('December'), _('December')),
        )

    harvest_month = models.CharField(
        choices=MONTHS,
        verbose_name=_('Harvest month'),
        max_length=9,
    )

    def __str__(self):
        return f'{self.harvest_month}'

    @staticmethod
    def valid_months():
        """
        This class method returns a list of valid address
        types
        """
        return [k for k, v in HarvestMonth.MONTHS]
