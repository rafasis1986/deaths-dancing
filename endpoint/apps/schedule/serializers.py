from rest_framework_json_api import serializers
from apps.schedule.models import Booking
from apps.base.serializers import ClientSerializer


class BookingSerializer(serializers.HyperlinkedModelSerializer):
    included_serializers = {
        'client': ClientSerializer,
    }

    class Meta:
        model = Booking
        fields = ('id', 'client', 'created_ts', 'time',)

    class JSONAPIMeta:
        included_resources = ['client']


class BookingCreateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = ('time',)
