from rest_framework import serializers
from .models import SumpReading


class SumpReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SumpReading
        fields = "__all__"
