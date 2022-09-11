from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.models import Group

admin.site.site_title = "森田塾　管理サイト"
admin.site.site_header = "森田塾　管理サイト"
admin.site.index_title = "メニュー"
admin.site.unregister(Group)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')), 
    path('', include('accounts.urls')),
    path('summernote/', include('django_summernote.urls')),
]
