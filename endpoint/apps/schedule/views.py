from rest_framework import viewsets, status
from apps.schedule.serializers import BookingSerializer, BookingCreateSerializer
from apps.schedule.models import Booking
from rest_framework.response import Response


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        self.serializer_class = BookingCreateSerializer
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        booking = Booking()
        booking.client = request.user
        booking.time = request.data.get('time')
        booking.save()
        serializer = self.get_serializer(booking)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    # return viewsets.ModelViewSet.create(self, request, *args, **kwargs)
