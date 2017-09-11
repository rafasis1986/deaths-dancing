from django.db import models

from apps.base.models import Client
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid


class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    date = models.DateField(db_index=True)
    hour = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(17),
            MinValueValidator(9)])
    client = models.ForeignKey(Client)
    created_ts = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'schedule_booking'
        ordering = ['date', 'hour']

    class JSONAPIMeta:
        resource_name = 'booking'
