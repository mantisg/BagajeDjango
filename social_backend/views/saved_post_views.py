from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..serializers.saved_post_serializers import SavedPostSerializer
from ..models import Post, SavedPost

class ToggleSavedPostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):

        post = Post.objects.get(id=post_id)

        saved = SavedPost.objects.filter(
            user=request.user,
            post=post
        ).first()

        if saved:
            saved.delete()

            return Response({
                'status': 'unsaved'
            })

        SavedPost.objects.create(
            user=request.user,
            post=post
        )

        return Response({
            'status': 'saved'
        })
    
class SavedPostListView(generics.ListAPIView):
    serializer_class = SavedPostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return SavedPost.objects.filter(
            user=self.request.user
        ).select_related(
            'post'
        ).order_by(
            '-created_at'
        )