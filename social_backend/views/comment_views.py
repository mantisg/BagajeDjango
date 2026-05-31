from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ..models import Post, Comment
from ..serializers.comment_serializers import CommentSerializer
from ..permissions import IsCommentOwnerOrCreator


class PostCommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):

        slug = self.kwargs['slug']

        return Comment.objects.filter(
            post__slug=slug,
            is_deleted=False
        ).order_by('created_at')

    def perform_create(self, serializer):

        slug = self.kwargs['slug']

        post = Post.objects.get(slug=slug)

        serializer.save(
            author=self.request.user,
            post=post
        )

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsCommentOwnerOrCreator]