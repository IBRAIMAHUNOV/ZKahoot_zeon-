from django.contrib import admin
from django.urls import path, include, re_path
from fastest.serializers import GroupSerializer, LoginSerializer
from rest_framework import routers, serializers, viewsets
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_swagger.views import get_swagger_view
from fastest.views import UsersList, LoginAPIView, GroupsList
from quiz.views import QuizViewSet, AnswerViewSet, QuestionViewSet
from .yasg import *


urlpatterns = [
    re_path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('fastest/', include('fastest.urls')),  # app urls
    path('quiz/', include('quiz.urls')),
    path('users/', UsersList.as_view()),  # users views
    path('groups/', GroupsList.as_view()),  # groups views
    # path('', LoginAPIView.as_view()),  # users view
    path('nested_admin/', include('nested_admin.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
