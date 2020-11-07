from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from main import models


# client = Client()
#


class APITests(APITestCase):
    def setUp(self) -> None:
        client = models.Client.objects.create(fio='Иванов Максим Андреевич', number='12345678911')
        responsible = models.Responsible.objects.create(fio='Никитин Александ Николаевич', position='слесарь')
        responsible_second =models.Responsible.objects.create(fio='Мидлов Михаил Николаевич', position='слесарь')
        bid = models.Bid.objects.create(text='Тестовая заяака 1', responsible=responsible, client=client)
        self.bid_id = bid.id
        self.responsible_second_id = responsible_second.id
        self.responsible_id = responsible.id
        self.client_id = client.id


    def test_create_bid(self) -> None:
        url = 'http://127.0.0.1:8000/bid/up/'
        data = {
            "text": "Тестовая заявка 2",
            "responsible": self.responsible_id,
            "client": self.client_id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('id' in response.data)
        self.assertTrue('text' in response.data)
        self.assertTrue('date' in response.data)
        self.assertTrue('responsible' in response.data)
        self.assertTrue('client' in response.data)
        self.assertEqual(models.Bid.objects.count(), 2)

    def test_a_get_bid(self):
        url = 'http://127.0.0.1:8000/bid/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('id' in response.data[0])
        self.assertTrue('text' in response.data[0])
        self.assertTrue('date' in response.data[0])
        self.assertTrue('responsible' in response.data[0])
        self.assertTrue('client' in response.data[0])



    def test_update_bid(self):

        url = f'http://127.0.0.1:8000/bid/up/{self.bid_id}/'
        data = {
            "text": "Тестовая заява 3",
            "responsible": self.responsible_second_id,
            "client": 4
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('id' in response.data)
        self.assertTrue('text' in response.data)
        self.assertTrue('date' in response.data)
        self.assertTrue('responsible' in response.data)
        self.assertTrue('client' in response.data)
        bid = models.Bid.objects.get(id=self.bid_id)
        self.assertEqual(bid.responsible.id, self.responsible_second_id)
        self.assertEqual(response.data['text'], "Тестовая заява 3")

    def test_delite_bid(self):
        url = f'http://127.0.0.1:8000/bid/{self.bid_id}/'
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(models.Bid.objects.count(), 0)






# Create your tests here.
