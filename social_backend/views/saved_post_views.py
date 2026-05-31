from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
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