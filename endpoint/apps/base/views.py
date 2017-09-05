from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.base.models import Client
import apps.base.serializers as s


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = s.ClientSerializer


class MeView(GenericViewSet, RetrieveModelMixin):
    queryset = Client.objects.all()
    serializer_class = s.MeSerializer

    def get_object(self):
        return get_object_or_404(self.queryset, pk=self.request.user.id)
