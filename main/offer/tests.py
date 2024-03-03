from django.test import TestCase
from django.contrib.auth.models import User
from .forms import OfferForm
from django.contrib.auth.password_validation import validate_password

class PublishOfferTestCase(TestCase):
    def setUp(self):
        self.user = User()
        self.user.username = 'testuser'

        password = 'testpassword'
        validate_password(password)

        self.user.set_password(password)

    def test_valid_publish_offer_form(self):
        form_data = {
            'title': 'Test Offer',
            'offer_type': 'CO',
            'client': 'DF',
            'description': 'This is a test offer description.',
            'price_per_hour': 10.50,
            'city': 'Test City'
        }
        form = OfferForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_publish_offer_form_blank_string(self):
        form_data = {
            'title': '',  # Falta el titulo
            'offer_type': 'CO',
            'client': 'DF',
            'description': 'This is a test offer description.',
            'price_per_hour': 10.50,
            'city': 'Test City'
        }
        form = OfferForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_publish_offer_form_negative_price(self):
        form_data = {
            'title': 'Test Offer',
            'offer_type': 'CO',
            'client': 'DF',
            'description': 'This is a test offer description.',
            'price_per_hour': -10.50,  # Precio negativo
            'city': 'Test City'
        }
        form = OfferForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_publish_offer_form_invalid_enum(self):
        form_data = {
            'title': 'Test Offer',
            'offer_type': 'prueba', # Incorrecto
            'client': 'DF',
            'description': 'This is a test offer description.',
            'price_per_hour': 10.50,
            'city': 'Test City'
        }
        form = OfferForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_publish_offer_without_permission(self):
        form_data = {
            'title': 'Test Offer',
            'offer_type': 'CO',
            'client': 'DF',
            'description': 'This is a test offer description.',
            'price_per_hour': 10.50,
            'city': 'Test City'
        }
        form = OfferForm(data=form_data)
        self.assertTrue(form.is_valid())

        response = self.client.post('/offer/', form_data)
        self.assertEqual(response.status_code, 302)  # Redireccion a login
