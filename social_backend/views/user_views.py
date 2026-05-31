from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ..models import User
from ..serializers.user_serializers import UserSerializer, PublicUserSerializer

class CurrentUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
class UserProfileView(
    generics.RetrieveAPIView
):

    serializer_class = PublicUserSerializer
    lookup_field = 'slug'

    queryset = User.objects.all()