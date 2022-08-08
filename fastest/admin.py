from django.contrib import admin
from .models import UserModels
# from django.contrib.auth.models import Group


@admin.register(UserModels)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'groups', 'email',
                    'phone_number', 'image', 'rating',
                    'passed_test', 'is_staff', 'is_active']

    search_fields = ['username', 'group', 'phone_number']

    # class Meta:
    #     model = UserModels
    # list_filter = ('Date Created', 'Date Updated')


# select_related = ('username', 'lastname', 'phone_number')
# class ArticleAdmin(UserModels):
#     list_select_related = ('username', 'lastname', 'phone_number')

# admin.site.register(UserModels)
