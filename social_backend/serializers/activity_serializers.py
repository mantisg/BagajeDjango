from rest_framework import serializers
from ..models import UserActivity

class UserActivitySerializer(serializers.ModelSerializer):
    post_title = serializers.CharField(
        source='post.title',
        read_only=True
    )

    class Meta:
        model = UserActivity

        fields = [
            'id',
            'activity_type',
            'post_title',
            'created_at',
        ]