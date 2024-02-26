from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Offer

class OffersTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')

        self.offer1 = Offer.objects.create(title="Oferta 1", offer_type="CO", client="DF", description="Descripción de la Oferta 1", price_per_hour=50, city="Nueva York", available=True, user=self.user)
        self.offer2 = Offer.objects.create(title="Oferta 2", offer_type="CU", client="DM", description="Descripción de la Oferta 2", price_per_hour=60, city="Los Ángeles", available=True, user=self.user)
        self.offer3 = Offer.objects.create(title="Oferta 3", offer_type="TR", client="AN", description="Descripción de la Oferta 3", price_per_hour=40, city="Barcelona", available=True, user=self.user)
        self.offer4 = Offer.objects.create(title="Oferta 4", offer_type="DO", client="NI", description="Descripción de la Oferta 4", price_per_hour=70, city="Madrid", available=True, user=self.user)
        self.offer5 = Offer.objects.create(title="Oferta 5", offer_type="OT", client="OT", description="Descripción de la Oferta 5", price_per_hour=55, city="Sevilla", available=True, user=self.user)
        self.offer6 = Offer.objects.create(title="Oferta 6", offer_type="CO", client="DM", description="Descripción de la Oferta 6", price_per_hour=65, city="Valencia", available=True, user=self.user)
        self.offer7 = Offer.objects.create(title="Oferta 7", offer_type="CU", client="AN", description="Descripción de la Oferta 7", price_per_hour=45, city="Bilbao", available=True, user=self.user)

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

    def test_offer_detail(self):
        response = self.client.get(reverse('offer:detail', args=(self.offer1.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'offers/detail.html')
        self.assertContains(response, self.offer1.title)
        self.assertNotContains(response, self.offer2.title)

    def test_search_offers(self):
        response = self.client.post(reverse('offer:searchOffers'), {'search_query': 'Nueva York'})
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
