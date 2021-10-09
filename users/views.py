from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from .models import User
from .serializers import CreateEditSerializer, DetailListSerializer
# Create your views here.

@api_view(['GET'])
def list(request):
    users = User.objects.filter(User.isDeleted).order_by('name')
    serializer = DetailListSerializer(users, many=True)
    return HttpResponse(serializer.data)

@api_view(['POST'])
def create(request):
    serializer = CreateEditSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return HttpResponse(status=200)

@api_view(['PUT'])
def edit(request, pk):
    try:
        user = User.objects.get(id=pk)
        serializer = CreateEditSerializer(instance=user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status=200)
    except User.DoesNotExist:
        raise Http404

@api_view(['GET'])
def detail(request, pk):
    try:
        user = User.objects.get(id=pk)
        serializer = DetailListSerializer(user, many=False)
        return HttpResponse(serializer.data)
    except User.DoesNotExist:
        raise Http404

@api_view(['DELETE'])
def delete(request, pk):
    try:
        user = User.objects.get(id=pk)
        user.isDeleted = True
        user.save()
        return HttpResponse(status=204)
    except User.DoesNotExist:
        raise Http404