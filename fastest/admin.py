from django.contrib import admin
from .models import UserModels, Group
# from nested_inline.admin import NestedModelAdmin

@admin.register(UserModels)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'groups', 'email',
                    'phone_number', 'image',
                    'rating_group', 'rating_global', 'score',
                    'is_staff', 'is_active']

    search_fields = ['username', 'phone_number']
    list_filter = ('groups',)

#
# @admin.register(Group)
# class GroupAdmin(admin.ModelAdmin):
#     list_filter = ['groups']
