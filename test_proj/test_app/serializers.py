from .models import Client
from rest_framework import serializers


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ("url", "username", "first_name", "last_name", "birth_date",
                  "rating", "avatar")
