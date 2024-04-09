# myapp/serializers.py
from rest_framework import serializers
from .models import TestData

class TestDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestData
        fields = ['url', 'json_data']

    def to_representation(self, instance):
        return instance.json_data
