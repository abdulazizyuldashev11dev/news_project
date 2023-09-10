from django.contrib import admin
from .models import Category, News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'published_date']
    list_filter = ['status', 'created_date', 'published_date']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'
    search_fields = ['title', 'body']
    ordering = ['status', 'published_date']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']