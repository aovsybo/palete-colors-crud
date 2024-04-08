import re
import requests

from django.db import models
from django.conf import settings
from rest_framework.exceptions import ValidationError

from model_utils import FieldTracker


class Palete(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Color(models.Model):
    palete = models.ForeignKey(Palete, on_delete=models.CASCADE)
    color_hex = models.CharField(max_length=7)
    title = models.CharField(max_length=255)

    tracker = FieldTracker(fields=['color_hex'])

    def clean(self):
        super().clean()
        if not self.is_valid_hex(self.color_hex):
            raise ValidationError('Invalid hexadecimal color code')

    def save(self, *args, **kwargs):
        if self.color_hex and (not self.pk or self.tracker.has_changed('color_hex')):
            color_name = self.get_color_name(self.color_hex)
            if color_name:
                self.title = color_name
            else:
                raise ValidationError('Unable to fetch color name')

        super().save(*args, **kwargs)

    @staticmethod
    def is_valid_hex(color_hex):
        return re.match(r'^#[0-9A-Fa-f]{6}$', color_hex) is not None

    @staticmethod
    def get_color_name(color_hex):
        url = f'https://www.thecolorapi.com/id?hex={color_hex[1:]}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get('name', {}).get('value')
        return None
