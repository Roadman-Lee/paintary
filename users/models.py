from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"
    nickname = models.CharField(max_length=50)
    username = models.CharField(max_length=30, unique=False)
    email = models.EmailField(unique=True)
