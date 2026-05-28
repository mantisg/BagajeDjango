from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from backend.social_backend.permissions import IsCreatorOrReadOnly
from .models import Post, Reaction, Comment, UserActivity
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsCreatorOrReadOnly]

class ToggleReactionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        reaction_type = request.data.get('reaction_type')

        post = Post.objects.get(id=post_id)

        existing_reaction = Reaction.objects.filter(
            post=post,
            user=request.user
        ).first()

        # No reaction exists → create one
        if not existing_reaction:
            Reaction.objects.create(
                post=post,
                user=request.user,
                reaction_type=reaction_type
            )

            return Response({
                'status': 'created',
                'reaction': reaction_type
            })

        # Same reaction clicked again → remove it
        if existing_reaction.reaction_type == reaction_type:
            existing_reaction.delete()

            return Response({
                'status': 'removed'
            })

        # Different reaction → update it
        existing_reaction.reaction_type = reaction_type
        existing_reaction.save()

        return Response({
            'status': 'updated',
            'reaction': reaction_type
        })