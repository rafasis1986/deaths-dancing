from django.conf.urls import url, include
from rest_framework import routers
from apps.schedule import views
from apps.schedule.views import HourlyAvaliables

router = routers.DefaultRouter()
router.register(r'bookings', views.BookingViewSet)

urlpatterns = [
    url(r'^schedule/', include(router.urls)),
    url(r'^avaliable/hours/', HourlyAvaliables.as_view()),
]
