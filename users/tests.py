from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User


class UserTest(APITestCase):

    def test_create_user(self):
        url = reverse('create-user')
        user = {'username' : "test_user"}
        response = self.client.post(url, data=user, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user2 = {"username" : "test user"}
        response2 = self.client.post(url, data=user2, format='json')
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)

    
    def test_retrieve_user(self):
        user = User.objects.create(username='Hassan202')
        url = f'{reverse('retrieve-user')}?username={user.username}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], user.username)

        url2 = f'{reverse('retrieve-user')}?id={user.id}'
        response2 = self.client.get(url2)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.data['id'], user.id)

        url3 = f'{reverse('retrieve-user')}?username=non-user'
        response3 = self.client.get(url3)
        self.assertEqual(response3.status_code, status.HTTP_404_NOT_FOUND)



    def test_update_user(self):
        user = User.objects.create(username='user1')
        data = {"username" : "new-user"}
        url = f"{reverse("update-user")}?username={user.username}"
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'new-user')

        url2 = f"{reverse("update-user")}?id={user.id}"
        response2 = self.client.put(url2, data, format='json')
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.data['username'], 'new-user')

    def test_delete_user(self):
        user = User.objects.create(username='user1')
        url = f"{reverse("delete-user")}?username={user.username}"
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url2 = f"{reverse("delete-user")}?id={user.id}"
        response2 = self.client.delete(url2, format='json')
        self.assertEqual(response2.status_code, status.HTTP_200_OK)

        url3 = f"{reverse("delete-user")}?idss={user.id}"
        response3 = self.client.delete(url3, format='json')
        self.assertEqual(response3.status_code, status.HTTP_404_NOT_FOUND)