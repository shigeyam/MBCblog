from django.contrib import admin
from .models import Post, Comment, Meeting, ImageUpload
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Meeting)
admin.site.register(ImageUpload)

