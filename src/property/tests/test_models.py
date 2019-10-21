from django.utils.translation import ugettext as _
from localflavor.br.br_states import STATE_CHOICES
from django.test import TestCase
from ..models import Property
from users.models import User

class PropertyModelTest(TestCase):

    def setUp(self):
        user = User.objects.create(
            email='vitas@vitas.com',
            password='vitas'
        )

        self.obj = Property.objects.create(
            type_of_address='House',
            BRZipCode='71021491',
            state='DF',
            city='Gama',
            district='Setor Leste',
            address='Quadra 4',
            complement='Casa 7B',
            owner = user
        )

    def test_verbose_name_plural(self):
        self.assertEqual(
            str(Property._meta.verbose_name_plural),
            _('Properties')
        )
    
    def test_property_creation(self):
        self.assertEqual(
            Property.objects.last(),
            self.obj,
            msg='Property is not being saved properly'
        )

    def test_string_representation(self):
        expected = (f'{self.obj.state}, ' +
            f'{self.obj.city}, {self.obj.address}')
        
        self.assertEqual(str(self.obj), expected)

    def test_valid_address(self):
        expected = [
            'Apartment',
            'House',
            'Farm',
            'Other',
        ]

        self.assertEquals(
            expected, 
            Property.valid_address()
        )
    
    def test_valid_states(self):
        expected = [k for k, v in STATE_CHOICES]

        self.assertEquals(
            expected, 
            Property.valid_states()
        )