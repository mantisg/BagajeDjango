from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from ..models import Post
from ..permissions import IsCreatorOrReadOnly
from ..serializers.post_serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsCreatorOrReadOnly]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = [
        'is_published',
    ]

    search_fields = [
        'title',
        'content',
    ]

    ordering_fields = [
        'created_at',
        'updated_at',
    ]

    def get_queryset(self):
        queryset = Post.objects.select_related(
            'author'
        )

        author = self.request.query_params.get(
            'author'
        )

        if author:
            queryset = queryset.filter(
                author__slug=author
            )

        return queryset.order_by(
            '-created_at'
        )
    
    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(
            request,
            *args,
            **kwargs
        )

        if request.user.is_authenticated:

            post = self.get_object()

            log_activity(
                request.user,
                post,
                'view'
            )

        return response