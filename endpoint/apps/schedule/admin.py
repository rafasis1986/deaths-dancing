from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    queryset = Booking.objects.all()
    list_display = ('client', 'created_ts', 'id', 'time',)


admin.site.register(Booking, BookingAdmin)
