from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import status

from .models import Identifier
from .serializers import IdentifierSerializer
from .service import Generator

# Create your views here.
class GetIdentifierView(APIView, Generator):
    """
    generates a random uuid and returns a
    list of all uuids in the system
    """
    def get(self):
        timestamp = self.getTimestamp()
        uId = self.getUid()
        Identifier.objects.create(
            uniqueId = { f"{timestamp}": f"{uId}"},
            createdAt = timestamp
        )
        identifiers = Identifier.objects.all()
        return Response(identifiers)
