from django.contrib import admin
from .models import Post, Comment, Meeting, ImageUpload

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Meeting)
admin.site.register(ImageUpload)
