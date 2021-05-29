import datetime
import uuid

from django.test import TestCase

from src.models import Identifier
from src.service import Generator


class IdentifierTestCase(TestCase):

    def __init__(self):
        self.generator = Generator()

    def test_identifier(self):
        self.assertEquals(
            Identifier.objects.count(), 0
        )
        timestamp = self.generator.getTimestamp()
        uId = self.generator.getUid()
        Identifier.objects.create(
            uniqueId = { f"{timestamp}": f"{uId}"},
            createdAt = timestamp
        )
        self.assertEquals(
            Identifier.objects.count(), 1
        )
        
