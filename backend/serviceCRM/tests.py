from django.test import TestCase, RequestFactory
from django.urls import reverse
from .models import Insert
from .views import InsertListView, InsertNew, Update, Nalog, Done

class InsertListViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/list/')  # replace with your actual url
        self.assertEqual(response.status_code, 200)

class InsertNewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/insert/')  # replace with your actual url
        self.assertEqual(response.status_code, 200)

class UpdateTest(TestCase):
    def setUp(self):
        self.insert = Insert.objects.create(name="Test", phone="1234567890", description="Test description", done=False, repair="Test repair")

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse('update', args=(self.insert.id,)))  # replace 'update' with your actual url name
        self.assertEqual(response.status_code, 200)

class NalogTest(TestCase):
    def setUp(self):
        self.insert = Insert.objects.create(name="Test", phone="1234567890", description="Test description", done=False, repair="Test repair")

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse('/nalog/', args=(self.insert.id,)))  # replace 'nalog' with your actual url name
        self.assertEqual(response.status_code, 200)

class DoneTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/done/')  # replace with your actual url
        self.assertEqual(response.status_code, 200)