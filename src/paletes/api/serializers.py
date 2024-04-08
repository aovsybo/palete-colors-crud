from rest_framework import serializers

from ..models import Palete, Color


class PaleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palete
        exclude = ('user',)


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        exclude = ('palete',)

    def validate(self, attrs):
        if 'title' not in attrs:
            raise serializers.ValidationError("Title is required")
        return attrs
