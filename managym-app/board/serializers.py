from rest_framework import serializers

from .models import Event, TargetResult, Athlete

class TargetResultSerializer(serializers.ModelSerializer):
    """Serializer representing the TargetResult model"""
    class Meta:
        model = TargetResult
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    """Serializer representing the Event model"""
    class Meta:
        model = Event
        fields = '__all__'


class AthleteSerializer(serializers.ModelSerializer):
    """Serializer representing the Athlete model"""
    class Meta:
        model = Athlete
        fields = '__all__'
        