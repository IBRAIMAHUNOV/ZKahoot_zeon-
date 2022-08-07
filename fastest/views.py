from django.contrib.auth.models import Group
from rest_framework import viewsets, permissions, generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from fastest.serializers import UserSerializer, GroupSerializer
from .serializers import LoginSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginAPIView(APIView):

    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)


# class UserViewSet(viewsets.ModelViewSet):
#     """Конечная точка API, которая позволяет пользователям менять, просматривать"""
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permissions_classes = [permissions.IsAuthenticated]
#
#
# class GroupViewSet(viewsets.ModelViewSet):f
#     """Конечная точка API, которая позволяет группам менять, просматривать"""
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]
