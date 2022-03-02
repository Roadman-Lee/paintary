from django.urls import path
from . import views
from .views import Profile, UpdateProfile

urlpatterns = [
    path('sign-up/', views.sign_up_view, name='sign-up'),
    path('sign-in/', views.sign_in_view, name='sign-in'),
    path('profile/', views.Profile, name='profile'),
    path('profile/update', UpdateProfile.as_view(), name='profile_update'),
    path('find-password/', views.find_password, name='find-password'),
    path('v-password/', views.verification_email_code, name='v-password'),
    path('set-password/', views.set_password, name='set-password'),
]

