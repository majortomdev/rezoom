from rest_framework import viewsets
from .models import User, UrlObject
from .serializers import UserSerialiazer, UrlobjectSerializer

class UserViewSet(viewsets.ModelViewSet):
        queryset = User.objects.all()
        serializer_class = UserSerialiazer

class UrlobjectViewSet(viewsets.ModelViewSet):
        queryset = UrlObject.objects.all()
        serializer_class=UrlobjectSerializer