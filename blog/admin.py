from django.contrib import admin
from .models import Post, Comment, Meeting, ImageUpload, Category
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body')
    list_display = ('category', 'slug', 'title', 'posted_date')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'posted_date')

class MeetingAdmin(admin.ModelAdmin):
    list_display = ('name', 'posted_date')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Meeting, MeetingAdmin)
admin.site.register(ImageUpload)
admin.site.register(Category)
