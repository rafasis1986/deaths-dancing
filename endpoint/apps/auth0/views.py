import requests
import json

from django.conf import settings
from django.shortcuts import redirect
from rest_framework.decorators import permission_classes
import rest_framework_jwt.utils as jwt
from rest_framework.permissions import AllowAny

from apps.base.models import Client


@permission_classes((AllowAny, ))
def auth_callback(request):
    code = request.GET.get('code')
    json_header = {'content-type': 'application/json'}
    token_url = 'https://{0}/oauth/token'.format(settings.AUTH0_DOMAIN)
    token_payload = {
        'client_id': settings.AUTH0_CLIENT_ID,
        'client_secret': settings.AUTH0_CLIENT_SECRET,
        'redirect_uri': settings.AUTH0_REDIRECT_URI,
        'code': code,
        'grant_type': settings.AUTH0_GRANT_TYPE,
    }
    token_info = requests.post(
        token_url, data=json.dumps(token_payload), headers=json_header).json()
    user_url = 'https://{domain}/userinfo?access_token={access_token}'.format(
        domain=settings.AUTH0_DOMAIN,
        access_token=token_info['access_token'])
    user_info = requests.get(user_url).json()
    user, flag = Client.objects.get_or_create(username=user_info.get('email'))
    user.email = user.username
    user.picture = user_info.get('picture')
    user.is_social = user_info['identities'][0]['isSocial']
    user.provider = user_info['identities'][0]['provider']
    user.provider_id = user_info['identities'][0]['user_id']
    if user.provider.upper() == 'AUTH0':
        user.first_name = user_info['user_metadata']['family_name']
        user.last_name = user_info['user_metadata']['given_name']
    else:
        user.first_name = user_info.get('family_name')
        user.last_name = user_info.get('given_name')
        if user.first_name is None:
            user.first_name = user_info.get('name')
    user.save()
    payload = jwt.jwt_payload_handler(user)
    token = jwt.jwt_encode_handler(payload)
    response = redirect(settings.CLIENT_AUTH_RESPONSE_URL)
    response.set_cookie(key='auth_token', value=token, max_age=10)
    response.set_cookie(
        key='expiration_time',
        value=int(settings.JWT_AUTH.get('JWT_REFRESH_EXPIRATION_DELTA').total_seconds()),
        max_age=10)
    response.set_cookie(
        key='auth_prefix',
        value=settings.JWT_AUTH.get('JWT_AUTH_HEADER_PREFIX'),
        max_age=10)
    return response
