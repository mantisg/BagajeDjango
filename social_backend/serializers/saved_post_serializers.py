from rest_framework import serializers
from ..models import SavedPost

class SavedPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = SavedPost

        fields = [
            'id',
            'user',
            'post',
            'created_at',
        ]

        read_only_fields = [
            'user',
            'created_at',
        ]