from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from ..models import User
from ..serializers.auth_serializers import RegisterSerializer
from ..serializers.user_serializers import UserSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        serializer = RegisterSerializer(
            data=request.data
        )

        if serializer.is_valid():

            user = serializer.save()

            login(request, user)

            return Response(
                UserSerializer(user).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        username = request.data.get('username')

        password = request.data.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(request, user)

            return Response({
                'message': 'Login successful',
                'user': UserSerializer(user).data
            })

        return Response(
            {
                'error': 'Invalid credentials'
            },
            status=status.HTTP_401_UNAUTHORIZED
        )
    
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        logout(request)

        return Response({
            'message': 'Logged out successfully'
        })
    
class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        serializer = UserSerializer(
            request.user
        )

        return Response(serializer.data)