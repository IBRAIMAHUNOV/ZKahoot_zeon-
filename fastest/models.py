from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
# from .hashers import PBKDF2WrapperSHA1PasswordHasher
from django.contrib.auth.models import PermissionsMixin, Group
from django.contrib.auth.models import UserManager, BaseUserManager, AbstractUser
from quiz.models import QuizTaker
# from quiz.models import Quiz


class UserModels(AbstractUser):
    """Custom user model."""
    usernames = None
    groups = models.ForeignKey(Group, null=True, on_delete=models.CASCADE, related_name='groupp')
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(blank=True)
    image = models.ImageField(blank=True, null=True)
    score = models.FloatField(null=True, blank=True, default=0)
    passed_total_tests = models.PositiveIntegerField(default=0, null=True, blank=True)
    # passed_tests = models.ManyToManyField('quiz.Quiz', blank=True, related_name='passed_user_test')
    rating_group = models.IntegerField(default=0, null=True, blank=True, validators=[MinValueValidator(1)])
    rating_global = models.PositiveIntegerField(null=True, blank=True, validators=[MinValueValidator(1)])
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    class Meta:
        ordering = ['-rating_global']

    def has_module_perms(self, app_label):
        return self.is_staff

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        rate_glbl = QuizTaker.objects.all().filter(user=self)
        score = 0
        for qt in rate_glbl:
            score += qt.score

        self.rating_global = score
        super().save(*args, **kwargs)

        rate_grp = QuizTaker.objects.all().filter(user=self)
        score = 0
        for qt in rate_grp:
            score += qt.score

        self.rating_group = score
        super().save(*args, **kwargs)


class CustomUserManager(BaseUserManager):
    """Custom user manager"""
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Электронная почта должна быть установлена")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        elif extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)
