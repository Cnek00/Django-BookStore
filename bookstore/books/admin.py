from django.contrib import admin
from .models import Book , Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'stock', 'created_at')
    search_fields = ('title', 'author')
    list_filter = ('author', 'created_at','categories')
    ordering = ('-created_at',)
