from django.contrib.auth.models import User, Group
from .models import LineUp, Day, Event
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
	"""docstring for UserSerializer"""
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
	"""docstring for UserSerializer"""
	class Meta:
		model = Group
		fields = ('url', 'name')


class LineUpSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = LineUp
		fields = ('id', 'title', 'host', 'duration', 'about_program', 'lineup_image', 'lineup_thumbnail')

class DaySerializer(serializers.HyperlinkedModelSerializer):
	lineUp = LineUpSerializer(many=True)
	class Meta:
		model = Day
		fields = ('id', 'day', 'lineUp')

class EventSerializer(serializers.ModelSerializer):

	class Meta:
		model = Event
		fields = ('id', 'title', 'info', 'event_image', 'created')