from django.conf.urls import url
from apps.auth0.views import auth_callback


urlpatterns = [
    url(r'^callback/', auth_callback),
]
