from rest_framework import serializers

from .models import Identifier


class IdentifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Identifier
        fields = ('uniqueId')