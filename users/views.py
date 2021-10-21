import json

from django.core.exceptions import ValidationError
from django.db.models import query
from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework import generics, serializers, viewsets
from rest_framework.decorators import api_view

from .models import User
from .serializers import (CreateUpdateSerializer, ListRetrieveSerializer,
                          UserSerializer)

# Create your views here.

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUpdateSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = ListRetrieveSerializer

class UserRetrieve(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = ListRetrieveSerializer

class UserUpdate(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUpdateSerializer

class UserDelete(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = ListRetrieveSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ListUsers(generics.ListAPIView):

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
    serializer_class = UserSerializer
