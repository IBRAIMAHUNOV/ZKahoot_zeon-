from . import serializers
from django.urls import path
from quiz.views import QuizTakerViewset, QuizViewSet, QuestionViewSet, UsersAnswerViewset
# from .views import UsersAnswerViewSet


urlpatterns = [
#   path('checking/', UsersAnswerViewSet.as_view()),
    path('quizzez/', QuizViewSet.as_view()),
    path('quizzez/<int:pk>', QuizViewSet.as_view()),
    path('question/', QuestionViewSet.as_view()),
    path('questions/<int:pk>', QuestionViewSet.as_view()),
    path('quiztaker/', QuizTakerViewset.as_view()),
    path('count/', UsersAnswerViewset.as_view()),

#     path('quiz/', QuizViewSet.as_view()),
#     path('questions/', QuestionViewSet.as_view()),
#     path('answer/', AnswerViewSet.as_view()),
]