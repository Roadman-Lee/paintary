from django.db import models

# Create your models here.
class PostModel(models.Model):
    class Meta:
        db_table = "posts"

    user_id = models.CharField(max_length=200, null=False)
    post_file = models.FileField(upload_to='uploads/%Y/%m/%d')
    writing = models.TextField(max_length=200, null=False)
    postdate = models.DateTimeField(auto_now_add=True)
    like_cnt = models.IntegerField()

class CommentModel(models.Model):
    class Meta:
        db_table = "comments"

    user_id = models.CharField(max_length=200, null=False)
    post_id = models.CharField(max_length=200, null=False)
    comment = models.CharField(max_length=200, null=False)

class ScrapModel(models.Model):
    class Meta:
        db_table = "scraps"

    user_id = models.CharField(max_length=200, null=False)
    post_id = models.CharField(max_length=200, null=False)
