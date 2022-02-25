from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:postid>', views.detail, name='detail'),
    path('upload/<int:id>', views.upload, name='upload'),
]