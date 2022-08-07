from django.contrib import admin
import nested_admin
from .models import Quiz, Question, Answer, UsersAnswer, QuizTaker


class AnswerInline(nested_admin.NestedTabularInline):
    model = Answer
    extra = 4
    max_num = 4


class QuestionInline(nested_admin.NestedTabularInline):
    model = Question
    inlines = [AnswerInline, ]
    extra = 5


class QuizAdmin(nested_admin.NestedModelAdmin):
    inlines = [QuestionInline,]


class UserAnswerInline(admin.TabularInline):
    model = UsersAnswer


class QuizTakersAdmin(admin.ModelAdmin):
    inlines = [UserAnswerInline, ]


admin.site.register(Quiz)
admin.site.register(QuizTaker, QuizTakersAdmin)
admin.site.register(UsersAnswer)
