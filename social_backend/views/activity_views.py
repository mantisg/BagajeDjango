from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ..models import UserActivity
from ..serializers.activity_serializers import UserActivitySerializer

class MyActivityView(generics.ListAPIView):
    serializer_class = UserActivitySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return UserActivity.objects.filter(
            user=self.request.user
        ).select_related(
            'post'
        ).order_by(
            '-created_at'
        )