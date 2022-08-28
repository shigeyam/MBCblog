from django.urls import path
from blog.views import blog, frontpage, post_detail, mba_class, excel_class, commentpage
from MBCblog import settings
from django.contrib.staticfiles.urls import static
from .views import ImageUploadView


urlpatterns = [
    path("frontpage/", frontpage, name="frontpage"),
    path("blog/", blog, name="blog"),
    path("blog/<slug:slug>/", post_detail, name="post_detail"),
    path("mba_class/", mba_class, name="mba_class"),
    path("excel_class/", excel_class, name="excel_class"),
    path("commentpage/", commentpage , name="commentpage"),
    path("image-upload/", ImageUploadView.as_view(), name="image-upload"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
