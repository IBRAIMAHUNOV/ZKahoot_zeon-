from django.contrib.auth.models import Group
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
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


class UsersList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    search_fields = '__all__'
    # filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    # filterset_fields = ['groups']


class GroupsList(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]
    search_fields = 'name'