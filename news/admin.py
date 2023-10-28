from django.contrib import admin
from . models import NewsItem


# Register your models here.
@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'points', 'created_at']
    search_fields = ['title', 'points']
