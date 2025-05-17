from django.shortcuts import render
from rest_framework import generics
from .models import Reminder
from .serializers import reminderSerializer
# Create your views here.

class ReminderList(generics.ListCreateAPIView):
    queryset=Reminder.objects.all()
    serializer_class=reminderSerializer

class ReminderDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field='id'
    queryset=Reminder
    serializer_class=reminderSerializer