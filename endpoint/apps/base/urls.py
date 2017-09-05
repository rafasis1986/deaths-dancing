from django.conf.urls import url, include
from rest_framework import routers

from apps.base import views


router = routers.DefaultRouter()
router.register(r'clients', views.ClientViewSet)

urlpatterns = [
    url(r'^base/', include(router.urls)),
    url(r'^base/me/', views.MeView.as_view({'get': 'retrieve'})),
]
