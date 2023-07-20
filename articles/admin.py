from django.contrib import admin
from .models import Articles


# Register your models here.
class ArticleSetting(admin.ModelAdmin):
    list_display = ['title', 'is_read']
    list_editable = ['is_read']
    list_filter = ['is_read']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Articles, ArticleSetting)
