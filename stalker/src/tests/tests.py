from datetime import datetime

from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework.views import status

from ..models import Identifier
from ..service import Generator


class TestGetIdentifierView(APITestCase):
    def __init__(self):
        self.generator = Generator()
        self.url = reverse('api-identifier', kwargs={'version':'v1'})
        self.mockData = [
            {
                "mockId":{"2021-05-28 22:26:38.511363":"3b877a8f-a1e3-47ff-bb3c-363cfbdc137c"},
                "mockTimestamp":datetime(2021, 5, 28, 22, 26, 38, 511363)
            },
            {
                "mockId":{"2021-05-28 22:24:11.370288":"78aa50a4-a81c-4d7b-b627-01afb46ed2b2"},
                "mockTimestamp":datetime(2021, 5, 28, 22, 24,11, 370288)
            },
            {
                "mockId":{"2021-05-28 22:28:45.266027":"1d7a03a6-3fab-42cf-8a59-08ef5aa0d88a"},
                "mockTimestamp":datetime(2021, 5, 28, 22, 28, 45, 266027)
            }
        ]

    def testGetIdentifier(self):
        for data in self.mockData:
            identifier = Identifier(
                uniqueId = data.mockId,
                createdAt = data.mockTimestamp
                )
            identifier.save()
        response = self.client.get(self.url)
        responseJson = response.json()
        self.assertEquals(
            len(responseJson), len(self.mockData)
        )
        firstResponse = responseJson.data[0]
        self.assertEquals(
            self.mockData[2].mockId, firstResponse
        )