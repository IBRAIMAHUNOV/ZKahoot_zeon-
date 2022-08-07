from django.urls import re_path as url
from django.urls import path
from  rest_framework_simplejwt.views import TokenVerifyView
from .api import RegisterApi
from .views import LoginAPIView


urlpatterns = [
    path('api/register', RegisterApi.as_view()),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify')
 ]
