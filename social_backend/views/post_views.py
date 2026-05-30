from rest_framework import viewsets
from ..models import Post
from ..permissions import IsCreatorOrReadOnly
from ..serializers.post_serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsCreatorOrReadOnly]
    lookup_field = 'slug'