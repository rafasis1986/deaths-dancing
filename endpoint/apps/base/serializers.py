from rest_framework_json_api import serializers
from apps.base.models import Client


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('id', 'username', 'email')
