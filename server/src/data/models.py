from django.core import validators
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone


class Data(models.Model):
    cpu_load = models.FloatField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    timestamp = models.DateTimeField(
        auto_now=True,
    )
    ip_address = models.CharField(max_length=15)

    def __repr__(self) -> str:
        return f'<Data {self.cpu_load} from {self.ip_address} at {self.timestamp.strftime("%d-%m-%d")}>'
