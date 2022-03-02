from django.urls import path
from .views import UploadFeed, BookmarkFeed


urlpatterns = [
    path('upload', UploadFeed.as_view(), name='upload_feed'),
    path('bookmark', BookmarkFeed.as_view(), name='bookmark'),
]