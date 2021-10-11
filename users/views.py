from django.db.models import query
from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from .models import User
from .serializers import CreateUpdateSerializer, ListRetrieveSerializer
from django.views import View
from django.core.exceptions import ValidationError
import json
from rest_framework import generics
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

