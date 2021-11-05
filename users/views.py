from rest_framework import generics
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.request import Request

from rest_framework.permissions import IsAuthenticated


class UserTestViewSet(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, *args, **kwargs):
        return Response({
            "message": "OK",
        })
