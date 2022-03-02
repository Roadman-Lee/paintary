from django.urls import path
from . import views
from .views import Profile, UpdateProfile

urlpatterns = [
    path('sign-up/', views.sign_up_view, name='sign-up'),
    path('sign-in/', views.sign_in_view, name='sign-in'),
    path('profile/update', UpdateProfile.as_view(), name='profile_update'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)