from django.contrib import admin
from . import models

@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'slug', 'author')
    prepopulated_fields = {'slug': ('title',),}

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "name", "email", "publish", "status")
    prepopulated_fields = {'status': ('publish',)}
    search_fields = ("name", "email", "content")


admin.site.register(models.Category)
