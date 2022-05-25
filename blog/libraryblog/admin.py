from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin 
from .models import *


class PostAdmin(SummernoteModelAdmin):
    list_display = ("post_title", "slug", "status", "created_on")
    list_filter = ("status", "created_on")
    search_fields = ["post_title", "content"]
    prepopulated_fields = {"slug": ("post_title",)}
 
    summernote_fields = ("content",)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "body", "post", "created_on", "active")
    list_filter = ("active", "created_on")
    search_fields = ("name", "email", "body")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Post, PostAdmin)