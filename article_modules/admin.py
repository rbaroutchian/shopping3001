from django.contrib import admin
# from . import models
from .models import ArticleComment,Article,ArticleCategory

class ArticleCommentadmin(admin.ModelAdmin):
    list_display = ['user', 'create_date', 'parent']

admin.site.register(Article)
admin.site.register(ArticleCategory)
admin.site.register(ArticleComment,ArticleCommentadmin)
