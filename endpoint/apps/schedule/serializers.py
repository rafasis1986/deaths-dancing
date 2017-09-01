from rest_framework_json_api import serializers
from apps.schedule.models import Booking


class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = ('id', 'client', 'created_ts', 'date', 'hour',)
