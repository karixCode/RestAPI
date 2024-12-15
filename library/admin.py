from django.contrib import admin
from .models import Author, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'biography')
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year', 'genre', 'category', 'publisher', 'is_textbook')
    list_filter = ('genre', 'category', 'publisher', 'is_textbook')
    search_fields = ('title', 'author__name', 'publisher')
    autocomplete_fields = ('author',)
