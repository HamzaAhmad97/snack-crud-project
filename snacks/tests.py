from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Snack

class SnackTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'John',
            email='test@gmail.com',
            password='something123'
        )
        self.snack = Snack.objects.create(
            title = 'Doritos',
            description = 'Tasty cripsy chips.',
            purchaser = self.user
        )

    def test_string_representation(self):
        snack = Snack(title = 'Galaxy Chocolate')
        self.assertEqual(str(snack), snack.title)

    def test_get_absolute_url(self):
        self.assertEqual(self.snack.get_absolute_url(), '/1/')

    def test_snack_fields(self):
        self.assertEqual(f'{self.snack.title}', 'Doritos')
        self.assertEqual(f'{self.snack.purchaser}', 'John')
        self.assertEqual(f'{self.snack.description}', 'Tasty cripsy chips.')

    def test_snack_detail_view(self):
        response = self.client.get('/1/')
        no_response = self.client.get('/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Tasty cripsy chips.')
        self.assertTemplateUsed(response, 'snacks/snack_detail.html')

    def test_snack_create_view(self): 
        response = self.client.post(reverse('snack_create'), {
            'title': 'some title',
            'description': 'some description',
            'purchaser': self.user.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Snack.objects.last().title, 'some title')
        self.assertEqual(Snack.objects.last().description, 'some description')

    def test_snack_update_view(self):
        response = self.client.post(reverse('snack_update', args='1'), {
            'title': 'Updated title',
            'description': 'Updated desc',
        })
        self.assertEqual(response.status_code, 302)

    def test_snack_delete_view(self): 
        response = self.client.post(
            reverse('snack_delete', args='1'))
        self.assertEqual(response.status_code, 302)

