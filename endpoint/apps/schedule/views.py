from rest_framework import viewsets, status
from apps.schedule.serializers import BookingSerializer, BookingCreateSerializer
from apps.schedule.models import Booking
from rest_framework.response import Response
from filters.mixins import FiltersMixin
from apps.schedule.validations import bookings_query_schema
from rest_framework.views import APIView
from datetime import datetime
from rest_framework.settings import api_settings


class BookingViewSet(FiltersMixin, viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    ordering = ('date', 'hour',)
    filter_validation_schema = bookings_query_schema
    filter_mappings = {
        'date_gt': 'date__gte',
        'date_lt': 'date__lt',
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
        booking.date = request.data.get('date')
        booking.hour = request.data.get('hour')
        booking.save()
        serializer = self.get_serializer(booking)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class HourlyAvaliables(APIView):
    allowed_methods = ['get']

    def get(self, request, *args, **kwargs):
        availability_list = []
        if self.request.query_params.get('date'):
            date_param = self.request.query_params.get('date')
            date = datetime.strptime(date_param, '%d/%m/%Y')
            busy = Booking.objects.filter(date=date).values_list('hour')
            busy_hours = [x[0] for x in busy]
            for i in range(9, 16):
                if i not in busy_hours:
                    availability_list.append(i)
        return Response({'availability': availability_list}, status=status.HTTP_200_OK)
