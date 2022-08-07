from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core import validators
from django.utils.translation import gettext_lazy as _
# from .hashers import PBKDF2WrapperSHA1PasswordHasher
from django.contrib.auth.models import PermissionsMixin, Group
from django.contrib.auth.models import UserManager, BaseUserManager, AbstractUser


class UserModels(AbstractUser):
    """Custom user model."""
    usernames = None
    groups = models.ForeignKey(Group, null=True, on_delete=models.CASCADE, related_name='groupp')
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(blank=True)
    image = models.ImageField(blank=True, null=True)
    rating = models.IntegerField(null=True, blank=True)
    passed_test = models.IntegerField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def has_module_perms(self, app_label):
        return self.is_staff

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def __str__(self):
        return self.email


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
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


# class UserModels(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(db_index=True, max_length=255, unique=True)
#     lastname = models.CharField(max_length=255, blank=True)
#     groups = models.ForeignKey(Group, null=True, on_delete=models.CASCADE, related_name='user_group')
#     phone_number = PhoneNumberField(blank=True)
#     email = models.EmailField(validators=[validators.validate_email], unique=True)
#     image = models.ImageField(blank=True, null=True)
#     rating = models.IntegerField(null=True, blank=True)
#     passed_test = models.IntegerField(null=True, blank=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#
#     objects = UserManager()
#
#     def has_module_perms(self, app_label):
#         return self.is_staff
#
#     def has_perm(self, perm, obj=None):
#         return self.is_staff
# #
#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'
#
#     def __str__(self):
#         return self.username

# class Group(models.Model):
#     """Class group user's"""
#     group_name = models.CharField(max_length=255)
#
#     class Meta:
#         verbose_name = 'Группа'
#         verbose_name_plural = 'Группы'
#
#     def __str__(self):
#         return self.group_name
