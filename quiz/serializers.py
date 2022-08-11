from rest_framework import routers, serializers, viewsets, generics
from quiz.models import Quiz, Question, Answer, QuizTaker, UsersAnswer
from fastest.models import UserModels


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    anzty = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'quiz', 'label', 'order', 'anzty']


class QuizSerializer(serializers.ModelSerializer):
    quezty = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = ['id', 'name', 'description', 'image', 'timestamp', 'quezty']


class QuizTakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizTaker
        fields = []


class QuestionResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'quezty', 'label', 'order']


class UsersAnswerSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    question_id = serializers.IntegerField()
    quiz_id = serializers.IntegerField()
    answer = serializers.CharField(max_length=185)
    order = serializers.IntegerField()
    submit = serializers.BooleanField(default=False)

    class Meta:
        model = UsersAnswer
        fields = '__all__'


