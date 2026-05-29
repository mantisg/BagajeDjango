from rest_framework import serializers

from ..models import Reaction

class ReactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reaction

        fields = [
            'id',
            'post',
            'user',
            'reaction_type',
            'created_at',
        ]

        read_only_fields = [
            'user',
            'created_at',
        ]