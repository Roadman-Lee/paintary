from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        db_table = "my_user"
    nickname = models.CharField(max_length=50)