from django.db import models

from apps.base.models import Client
import uuid


class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    time = models.DateTimeField(db_index=True, unique=True)
    client = models.ForeignKey(Client)
    created_ts = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'schedule_booking'

    class JSONAPIMeta:
        resource_name = 'booking'
