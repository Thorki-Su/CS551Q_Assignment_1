from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import Country, Data, Feedback

# Create your tests here.
class ModelTest(TestCase):
    def test_create_country(self):
        country = Country.objects.create(
            country_name="Testland",
            country_code="TST",
            region="Test Region",
            income_group="Test income",
            is_country=True
        )
        self.assertEqual(country.country_name, "Testland")
        self.assertEqual(country.country_code, "TST")
        self.assertEqual(country.region, "Test Region")
        self.assertTrue(country.is_country)

    def test_unique_country_code(self):
        Country.objects.create(country_name="A", country_code="A01")
        with self.assertRaises(IntegrityError):
            Country.objects.create(country_name="B", country_code="A01")

    def test_create_and_retrieve_data(self):
        country = Country.objects.create(country_name="DataLand", country_code="DL1")
        data = Data.objects.create(country=country, year=2020, emission=5.5)
        retrieved = Data.objects.get(country=country, year=2020)
        self.assertEqual(retrieved.emission, 5.5)

    def test_data_unique_together(self):
        country = Country.objects.create(country_name="UniqueLand", country_code="UNI")
        Data.objects.create(country=country, year=2000, emission=3.3)
        with self.assertRaises(IntegrityError):
            Data.objects.create(country=country, year=2000, emission=4.4)

    def test_feedback_str(self):
        fb = Feedback.objects.create(email="user@example.com", message="Great site!")
        self.assertIn("user@example.com", str(fb))
    
class ViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.country = Country.objects.create(country_name="Norway", country_code="NOR")
        Data.objects.create(country=self.country, year=2010, emission=12.5)

    def test_homepage(self):
        response = self.client.get(reverse('co2:homepage'))
        self.assertEqual(response.status_code, 200)

    def test_country_detail_view(self):
        response = self.client.get(reverse('co2:country_detail', args=[self.country.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "12.5")

    def test_map_view(self):
        response = self.client.get(reverse('co2:map'))
        self.assertEqual(response.status_code, 200)

class AuthTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass1234')

    def test_register_and_login(self):
        # register a user
        response = self.client.post(reverse('co2:register'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'complexpass123',
            'password2': 'complexpass123',
        })
        self.assertEqual(response.status_code, 302)
        # log-in the user
        login = self.client.login(username='newuser', password='complexpass123')
        self.assertTrue(login)

    def test_logout(self):
        self.client.login(username='testuser', password='pass1234')
        response = self.client.get(reverse('co2:logout'))
        self.assertEqual(response.status_code, 302)

class FeedbackViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_submit_feedback(self):
        response = self.client.post(reverse('co2:feedback'), {
            'email': 'lily@example.com',
            'feedback': 'Very informative website!',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Feedback.objects.count(), 1)
        self.assertEqual(Feedback.objects.first().email, 'lily@example.com')

class APITest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='chartuser', password='chartpass')
        self.client.login(username='chartuser', password='chartpass')
        self.country = Country.objects.create(country_name="Iceland", country_code="ICE")
        Data.objects.create(country=self.country, year=2005, emission=11.0)

    def test_country_emissions_api(self):
        response = self.client.get(reverse('co2:country_emissions_api', args=[self.country.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '11.0')

    def test_export_chart_png(self):
        response = self.client.get(reverse('co2:export_chart_png', args=[self.country.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'image/png')