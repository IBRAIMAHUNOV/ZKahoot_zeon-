# from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from quiz.serializers import (AnswerSerializer, QuestionSerializer, UsersAnswerSerializer,
                              QuizSerializer, QuizTakerSerializer)
from quiz.models import Quiz, Question, Answer, UsersAnswer, QuizTaker


class QuizViewSet(ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['name', 'description']


class QuestionViewSet(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['label']


class AnswerViewSet(ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]
    # search_fields = '__all__'


class QuizTakerViewset(ListAPIView):
    queryset = QuizTaker.objects.all()
    serializer_class = QuizTakerSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['score', 'user', 'quizz', 'answer', 'group']


class UsersAnswerViewset(ListAPIView):
    queryset = UsersAnswer.objects.all()
    serializer_class = UsersAnswerSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['user', 'question_id', 'answer',
                     'order', 'group', 'submit']