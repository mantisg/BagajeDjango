from rest_framework import serializers
from ..models import Comment

class CommentSerializer(serializers.ModelSerializer):

    author_username = serializers.CharField(
        source='author.username',
        read_only=True
    )

    author_profile_picture = serializers.ImageField(
        source='author.profile_picture',
        read_only=True
    )

    class Meta:
        model = Comment

        fields = [
            'id',
            'post',
            'author',
            'author_username',
            'author_profile_picture',
            'content',
            'created_at',
            'is_deleted',
        ]

        read_only_fields = [
            'author',
            'created_at',
        ]