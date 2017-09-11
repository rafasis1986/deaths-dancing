from rest_framework import viewsets, status
from apps.schedule.serializers import BookingSerializer, BookingCreateSerializer
from apps.schedule.models import Booking
from rest_framework.response import Response
from filters.mixins import FiltersMixin
from apps.schedule.validations import bookings_query_schema


class BookingViewSet(FiltersMixin, viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    ordering = ('time',)
    filter_validation_schema = bookings_query_schema
    filter_mappings = {
        'date_gt': 'time__gte',
        'date_lt': 'time__lt',
    }

    def get_queryset(self):
        query_params = self.request.query_params
        url_params = self.kwargs
        queryset_filters = self.get_db_filters(url_params, query_params)
        db_filters = queryset_filters['db_filters']
        queryset = Booking.objects.all()
        return queryset.filter(**db_filters)

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
