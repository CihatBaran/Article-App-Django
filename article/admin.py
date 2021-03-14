from django.contrib import admin

# Register your models here.
# import
from .models import Article

# register
# admin.site.register(Article)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created_date"]
    list_display_links = ["created_date"]
    search_fields = ["title"]

    list_filter = ["created_date"]

    class Meta:
        model = Article
