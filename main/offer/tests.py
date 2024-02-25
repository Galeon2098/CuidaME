from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Offer

class EditOfferTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.user2 = User.objects.create_user(username='testuser2', password='testpassword2')
        self.offer = Offer.objects.create(
            title='Original Title',
            offer_type='CO',
            client='DF',
            description='Original Description',
            price_per_hour=10.50,
            city='Original City',
            available=True,
            user=self.user
        )

    def test_edit_offer_authenticated_user_valid_data(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('offer:update', args=[self.offer.pk]), {
            'title': 'Updated Title',
            'offer_type': 'TR',
            'client': 'AN',
            'description': 'Updated Description',
            'price_per_hour': 15.75,
            'city': 'Updated City',
            'available': False
        })

        self.assertEqual(response.status_code, 200)
        updated_offer = Offer.objects.get(pk=self.offer.pk)
        self.assertEqual(updated_offer.title, 'Updated Title')
        self.assertEqual(updated_offer.offer_type, 'TR')
        self.assertEqual(updated_offer.client, 'AN')
        self.assertEqual(updated_offer.description, 'Updated Description')
        self.assertEqual(updated_offer.price_per_hour, 15.75)
        self.assertEqual(updated_offer.city, 'Updated City')
        self.assertTrue(updated_offer.available)

    def test_edit_offer_authenticated_user_invalid_data(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('offer:update', args=[self.offer.pk]), {
            'title': '',  # Title cannot be empty
            'offer_type': 'XX',  # Invalid offer type
            'client': 'XX',  # Invalid client type
            'description': 'Updated Description',
            'price_per_hour': -5.00,  # Invalid negative price
            'city': 'Updated City',
            'available': False
        })

        self.assertEqual(response.status_code, 200)  # Assuming you return to the same form for invalid data
        # Check if offer remains unchanged
        unchanged_offer = Offer.objects.get(pk=self.offer.pk)
        self.assertEqual(unchanged_offer.title, 'Original Title')
        self.assertEqual(unchanged_offer.offer_type, 'CO')
        self.assertEqual(unchanged_offer.client, 'DF')
        self.assertEqual(unchanged_offer.description, 'Original Description')
        self.assertEqual(unchanged_offer.price_per_hour, 10.50)
        self.assertEqual(unchanged_offer.city, 'Original City')
        self.assertTrue(unchanged_offer.available)

    def test_edit_offer_unauthenticated_user(self):
        response = self.client.post(reverse('offer:update', args=[self.offer.pk]), {
            'title': 'Attempted Title Update',
            'offer_type': 'DO',
            'client': 'NI',
            'description': 'Attempted Description Update',
            'price_per_hour': 20.00,
            'city': 'Attempted City Update',
            'available': False
        })
        self.assertRedirects(response, f'/login/?next=/offer/1/')

    def test_edit_offer_authenticated_user_invalid_data(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('offer:update', args=[self.offer.pk]), {
            'title': '',  # Title cannot be empty
            'offer_type': 'XX',  # Invalid offer type
            'client': 'XX',  # Invalid client type
            'description': 'Updated Description',
            'price_per_hour': -5.00,  # Invalid negative price
            'city': 'Updated City',
            'available': False
        })

    def test_edit_offer_invalid_user(self):
        self.client.login(username='testuser2', password='testpassword2')
        response = self.client.post(reverse('offer:update', args=[self.offer.pk]), {
            'title': 'Attempted Title Update',
            'offer_type': 'DO',
            'client': 'NI',
            'description': 'Attempted Description Update',
            'price_per_hour': 20.00,
            'city': 'Attempted City Update',
            'available': False
        })
        self.assertEqual(response.status_code, 403)
