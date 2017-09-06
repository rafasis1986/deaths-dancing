from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt import views


urlpatterns = [
    url('{0}/'.format(settings.M.API_VERSION), include([
        url(r'', include('apps.base.urls')),
        url(r'', include('apps.auth0.urls')),
        url(r'', include('apps.schedule.urls')),
        url(r'^admin/', admin.site.urls),
        url(r'^api-token-auth/', views.obtain_jwt_token),
        url(r'^api-token-verify/', views.verify_jwt_token),
        url(r'^api-token-refresh/', views.refresh_jwt_token),
    ])),
]
