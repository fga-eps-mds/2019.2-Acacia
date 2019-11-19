from django.test import TestCase
from harvest.models import Harvest, HarvestRules


class HarvestModelTest(TestCase):

    def test_valid_tree_types(self):
        expected = [
            'Done',
            'Cancelled',
            'Open',
            'Enough',
        ]

        self.assertEquals(
            expected,
            Harvest.valid_status()
        )


class HarvestRulesModelTest(TestCase):

    def test_unique_together(self):
        self.assertEqual(
            HarvestRules._meta.unique_together,
            (('harvest', 'description'),)
        )
