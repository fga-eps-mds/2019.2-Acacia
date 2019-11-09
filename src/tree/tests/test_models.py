from django.test import TestCase

from tree.models import HarvestMonth, Tree
from property.models import Property
from users.models import User


class TreeModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='vitas@vitas.com',
            password='vitas'
        )

        self.property = Property.objects.create(
            type_of_address='House',
            BRZipCode='71021491',
            state='DF',
            city='Gama',
            district='Setor Leste',
            address='Quadra 4',
            complement='Casa 7B',
            owner=self.user
        )

        self.tree = Tree.objects.create(
            property=self.property,
            tree_type='Pequizeiro',
            number_of_tree=3,
            tree_height=20.5,
        )

    def tearDown(self):
        self.property.delete()
        self.tree.delete()
        self.user.delete()

    def test_tree_creation(self):
        self.assertEqual(
            Tree.objects.last(),
            self.tree,
            msg='Tree is not being saved properly'
        )

    def test_valid_tree_types(self):
        expected = [
            'Avocado',
            'Pineapple',
            'Banana',
            'Persimmon',
            'Coconut',
            'FIG',
            'Guava',
            'Jabuticaba',
            'Orange',
            'Lemon',
            'Apple',
            'Papaya',
            'Mango',
            'Passion Fruit',
            'Quince',
            'Nectarine',
            'Loquat',
            'Pear',
            'Pequizeiro',
            'Tangerine',
            'Peach',
            'Vine'
        ]

        self.assertEquals(
            expected,
            Tree.valid_tree_types()
        )

    def test_string_representation(self):
        expected = (f"{self.tree.pk}, " +
                    f"{self.tree.tree_type}, " +
                    f"{self.tree.number_of_tree}")

        self.assertEqual(str(self.tree), expected)

    def test_unique_together(self):

        self.assertEqual(
            Tree._meta.unique_together,
            (('property', 'tree_type'),)
        )


class HarvestMonthModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='vitas@vitas.com',
            password='vitas'
        )

        self.property = Property.objects.create(
            type_of_address='House',
            BRZipCode='71021491',
            state='DF',
            city='Gama',
            district='Setor Leste',
            address='Quadra 4',
            complement='Casa 7B',
            owner=self.user
        )

        self.tree = Tree.objects.create(
            property=self.property,
            tree_type='Pequizeiro',
            number_of_tree=3,
            tree_height=20.5,
        )

        self.harvest_month = HarvestMonth.objects.create(
            tree=self.tree,
            harvest_month='September'
        )

    def tearDown(self):
        self.property.delete()
        self.tree.delete()
        self.user.delete()
        self.harvest_month.delete()

    def test_tree_creation(self):
        self.assertEqual(
            HarvestMonth.objects.last(),
            self.harvest_month,
            msg='HarvestMonth is not being saved properly'
        )

    def test_valid_tree_types(self):
        expected = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December'
        ]

        self.assertEquals(
            expected,
            HarvestMonth.valid_months()
        )

    def test_string_representation(self):
        expected = f'{self.harvest_month}'

        self.assertEqual(str(self.harvest_month), expected)

    def test_unique_together(self):

        self.assertEqual(
            HarvestMonth._meta.unique_together,
            (('tree', 'harvest_month'),)
        )
