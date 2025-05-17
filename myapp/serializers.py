from .models import Reminder
from rest_framework import serializers


class reminderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reminder
        fields='__all__'
