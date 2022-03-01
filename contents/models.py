from django.db import models
from django.conf import settings
from users.models import UserModel

# Create your models here.
class PostModel(models.Model):
    class Meta:
        db_table = "posts"

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='user_id')
    photo = models.URLField(max_length=200)
    writing = models.TextField(max_length=200, null=False)
    postdate = models.DateTimeField(auto_now_add=True)

class CommentModel(models.Model):
    class Meta:
        db_table = "comments"

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='user_id')
    post_id = models.ForeignKey(PostModel, on_delete=models.CASCADE, db_column='post_id')
    comment = models.CharField(max_length=200, null=False)

class ScrapModel(models.Model):
    class Meta:
        db_table = "scraps"

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='user_id')
    post_id = models.ForeignKey(PostModel, on_delete=models.CASCADE, db_column='post_id')
