from rest_framework import serializers
from ..models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = [
            'id',
            'username',
            'email',
            'slug',
            'profile_picture',
            'is_creator',
            'created_at',
        ]

        read_only_fields = [
            'id',
            'slug',
            'is_creator',
            'created_at',
        ]

class PublicUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = [
            'id',
            'username',
            'slug',
            'profile_picture',
            'is_creator',
        ]

        read_only_fields = [
            'id',
            'slug',
            'is_creator',
        ]