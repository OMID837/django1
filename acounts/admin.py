from django.contrib import admin
from .models import User
# Register your models here.
class UserSetting(admin.ModelAdmin):
    list_display = ['first_name', 'username', 'is_superuser', 'is_active']
    list_editable = ['is_superuser', 'is_active']
    list_filter = ['is_active']

admin.site.register(User, UserSetting)