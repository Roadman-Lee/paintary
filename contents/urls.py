from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:postid>', views.detail, name='detail'),
    path('detail/<int:postid>/delete', views.post_delete, name='delete'),
    path('detail/<int:postid>/edit', views.post_edit, name='edit'),
    path('upload/<int:id>', views.upload_view, name='upload'),
]
