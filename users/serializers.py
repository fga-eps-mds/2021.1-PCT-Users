from rest_framework import serializers
from users.models import User


class DetailListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email']

class CreateEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
