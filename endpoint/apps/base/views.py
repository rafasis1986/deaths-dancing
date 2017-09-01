from rest_framework import viewsets
from apps.base.models import Client
from apps.base.serializers import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
