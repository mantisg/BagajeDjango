from rest_framework import serializers
from ..models import Post

class PostSerializer(serializers.ModelSerializer):

    author_username = serializers.CharField(
        source='author.username',
        read_only=True
    )

    author_slug = serializers.CharField(
        source='author.slug',
        read_only=True
    )

    reaction_count = serializers.SerializerMethodField()

    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Post

        fields = [
            'id',
            'slug',
            'author',
            'author_username',
            'author_slug',
            'title',
            'content',
            'image',
            'video',
            'is_published',
            'reaction_count',
            'comment_count',
            'created_at',
            'updated_at',
        ]

        read_only_fields = [
            'author',
            'slug',
            'created_at',
            'updated_at',
        ]

    def get_reaction_count(self, obj):
        return obj.reactions.count()

    def get_comment_count(self, obj):
        return obj.comments.count()