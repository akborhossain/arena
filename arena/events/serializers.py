from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Event,EventRegistration

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'location', 'event_time']
        
class RegisterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=EventRegistration
        fields=['eid','registration_at','username']