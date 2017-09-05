import os
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

urlpatterns = [
    url(os.environ.get('DJANGO_URL_PREFIX', ''), include([
        url(r'', include('apps.base.urls')),
        url(r'', include('apps.auth0.urls')),
        url(r'', include('apps.schedule.urls')),
        url(r'^admin/', admin.site.urls),
        url(r'^api-token-auth/', obtain_jwt_token),
        url(r'^api-token-verify/', verify_jwt_token),
        url(r'^api-token-refresh/', refresh_jwt_token),
    ])),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
