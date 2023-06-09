from django.contrib import admin
from .models import Author, Category, Post, Comment, PostCategory, UserCategory


class PostCategoryInline(admin.TabularInline):
    model = PostCategory
    extra = 1


class UserCategoryInline(admin.TabularInline):
    model = UserCategory
    extra = 1


class PostAdmin(admin.ModelAdmin):
    inlines = [PostCategoryInline]


class CategoryAdmin(admin.ModelAdmin):
    inlines = [PostCategoryInline, UserCategoryInline]


admin.site.register(Author)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
