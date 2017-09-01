from rest_framework import viewsets
from apps.schedule.serializers import BookingSerializer
from apps.schedule.models import Booking


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
