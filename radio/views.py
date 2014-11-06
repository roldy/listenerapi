from django.shortcuts import render

from django.contrib.auth.models import User, Group
from .models import LineUp, Day, Event
from radio.serializers import UserSerializer, GroupSerializer, LineUpSerializer, DaySerializer, EventSerializer
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


# @api_view(('GET',))
# def api_root(request, format=None):
# 	return Response({
# 		'lineup': reverse('lineup-list', request=request, format=format)
# 		})

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer

class LineUpViewSet(viewsets.ModelViewSet):
	queryset = LineUp.objects.all()
	serializer_class = LineUpSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class DaysViewSet(viewsets.ModelViewSet):
	queryset = Day.objects.all()
	serializer_class = DaySerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class EventViewSet(viewsets.ModelViewSet):
	queryset = Event.objects.all()
	serializer_class = EventSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)