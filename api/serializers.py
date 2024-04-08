from rest_framework import serializers
from .models import TestData


class TestDataSerializer(serializers.Serializer):
    json_data = serializers.JSONField()

    def create(self, validated_data):
        # If you want to create a new row every time
        return TestData.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # If you want to overwrite existing data
        instance.json_data = validated_data.get('json_data', instance.json_data)
        instance.save()
        return instance
