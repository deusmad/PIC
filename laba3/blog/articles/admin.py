from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'get_excerpt', 'created_date')

    @admin.display(description='Текст')
    def get_excerpt(self, obj):
        if len(obj.text) > 80:
            return obj.text[:80] + "..."
        return obj.text
