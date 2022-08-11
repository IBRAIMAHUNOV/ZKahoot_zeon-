from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from wakanda import settings
# from .config import UserModels

UserModels = settings.AUTH_USER_MODEL


class Quiz(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=70)
    image = models.ImageField()
    roll_out = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    # group = models.ForeignKey(Group, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['timestamp', ]
        verbose_name_plural = 'Quizzes'

    def __str__(self):
        return self.name


    # def get_questions(self):
    #     return self.get_questions().all()


class Question(models.Model):
    label = models.CharField(max_length=100)
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE, related_name='quezty')
    order = models.IntegerField(default=20)

    def __str__(self):
        return self.label

    def get_answer(self):
        return self.anzty.all()

    def get_correct_answer(self):
        return self.anzty.get(correct=True)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='anzty')
    label = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.label


class QuizTaker(models.Model):
    user = models.ForeignKey(UserModels, on_delete=models.CASCADE, related_name='usser')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    score = models.FloatField(null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email

    def save(self, *args, **kwargs):
        self.user.save()
        super().save(*args, **kwargs)


class UsersAnswer(models.Model):
    quiz_taker = models.ForeignKey(QuizTaker, on_delete=models.CASCADE, null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True)
    score = models.FloatField(null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.question.label