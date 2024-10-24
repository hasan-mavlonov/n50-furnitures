from django.contrib import admin

from accounts.models import UserModel, UserManager


# Register your models here.
@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'is_active', 'date_joined',)
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('email', 'first_name', 'last_name')



# Register your models here.
