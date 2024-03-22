from django.test import TestCase, Client
from django.test import TestCase
from django.contrib.auth.models import User
from .forms import OfferForm
from django.contrib.auth.password_validation import validate_password
from django.test import TestCase
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
            poblacion='Sevilla',
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
            'poblacion': 'Tomares',
            'available': False
        })

        self.assertEqual(response.status_code, 302)
        updated_offer = Offer.objects.get(pk=self.offer.pk)
        self.assertEqual(updated_offer.title, 'Updated Title')
        self.assertEqual(updated_offer.offer_type, 'TR')
        self.assertEqual(updated_offer.client, 'AN')
        self.assertEqual(updated_offer.description, 'Updated Description')
        self.assertEqual(updated_offer.price_per_hour, 15.75)
        self.assertEqual(updated_offer.poblacion, 'Tomares')
        self.assertTrue(updated_offer.available)

    def test_edit_offer_authenticated_user_invalid_data(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('offer:update', args=[self.offer.pk]), {
            'title': '',  # Title cannot be empty
            'offer_type': 'XX',  # Invalid offer type
            'client': 'XX',  # Invalid client type
            'description': 'Updated Description',
            'price_per_hour': -5.00,  # Invalid negative price
            'poblacion': 'Tomares',
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
        self.assertEqual(unchanged_offer.poblacion, 'Sevilla')
        self.assertTrue(unchanged_offer.available)

    def test_edit_offer_unauthenticated_user(self):
        response = self.client.post(reverse('offer:update', args=[self.offer.pk]), {
            'title': 'Attempted Title Update',
            'offer_type': 'DO',
            'client': 'NI',
            'description': 'Attempted Description Update',
            'price_per_hour': 20.00,
            'poblacion': 'Bormujos',
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
            'poblacion': 'Tomares',
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
            'poblacion': 'Bormujos',
            'available': False
        })
        self.assertEqual(response.status_code, 403)


class PublishOfferTestCase(TestCase):
    def setUp(self):
        self.user = User()
        self.user.username = 'testuser'
        solotest = 'solotest'
        validate_password(solotest)

        self.user.set_password(solotest)

    def test_valid_publish_offer_form(self):
        form_data = {
            'title': 'Test Offer',
            'offer_type': 'CO',
            'client': 'DF',
            'description': 'This is a test offer description.',
            'price_per_hour': 10.50,
            'poblacion': 'Sevilla'
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
            'poblacion': 'Sevilla'
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
            'poblacion': 'Sevilla'
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
            'poblacion': 'Sevilla'
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
            'poblacion': 'Sevilla'
        }
        form = OfferForm(data=form_data)
        self.assertTrue(form.is_valid())

        response = self.client.post('/offer/', form_data)
        self.assertEqual(response.status_code, 302)  # Redireccion a login

class OffersTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')
        self.offer1 = Offer.objects.create(title="Oferta 1", offer_type="CO", client="DF", description="Descripción de la Oferta 1", price_per_hour=50, poblacion="Albaida del Aljarafe", available=True, user=self.user)
        self.offer2 = Offer.objects.create(title="Oferta 2", offer_type="CU", client="DM", description="Descripción de la Oferta 2", price_per_hour=60, poblacion="Alcalá de Guadaíra", available=True, user=self.user)
        self.offer3 = Offer.objects.create(title="Oferta 3", offer_type="TR", client="AN", description="Descripción de la Oferta 3", price_per_hour=40, poblacion="Alcalá del Río", available=True, user=self.user)
        self.offer4 = Offer.objects.create(title="Oferta 4", offer_type="DO", client="NI", description="Descripción de la Oferta 4", price_per_hour=70, poblacion="Algámitas", available=True, user=self.user)
        self.offer5 = Offer.objects.create(title="Oferta 5", offer_type="OT", client="OT", description="Descripción de la Oferta 5", price_per_hour=55, poblacion="Sevilla", available=True, user=self.user)
        self.offer6 = Offer.objects.create(title="Oferta 6", offer_type="CO", client="DM", description="Descripción de la Oferta 6", price_per_hour=65, poblacion="Almadén de la Plata", available=True, user=self.user)
        self.offer7 = Offer.objects.create(title="Oferta 7", offer_type="CU", client="AN", description="Descripción de la Oferta 7", price_per_hour=45, poblacion="Almensilla", available=True, user=self.user)

    def test_list_offers(self):
        response = self.client.get(reverse('offer:list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'offers/list.html')
        self.assertContains(response, self.offer1.title)
        self.assertContains(response, self.offer2.title)
        self.assertContains(response, self.offer3.title)
        self.assertContains(response, self.offer4.title)
        self.assertContains(response, self.offer5.title)
        self.assertContains(response, self.offer6.title)
        self.assertContains(response, self.offer7.title)

    # def test_offer_detail(self):
    #     response = self.client.get(reverse('offer:detail', args=(self.offer1.id,)))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'offers/detail.html')
    #     self.assertContains(response, self.offer1.title)
    #     self.assertNotContains(response, self.offer2.title)

    def test_search_offers(self):
        response = self.client.post(reverse('offer:searchOffers'), {'search_query': 'Albaida del Aljarafe'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'offers/search_results.html')
        self.assertContains(response, self.offer1.title)
        self.assertNotContains(response, self.offer2.title)

    def test_filter_offers(self):
        response = self.client.post(reverse('offer:filterOffers'), {'min_price_filter': 55})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'offers/list.html')
        self.assertNotContains(response, self.offer1.title)
        self.assertContains(response, self.offer2.title)

