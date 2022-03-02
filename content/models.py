from django.db import models

# Create your models here.
class Feed(models.Model):
    content = models.TextField()
    image = models.TextField()
    profile_image = models.TextField()
    email = models.EmailField(verbose_name='email', max_length=100, blank=True, null=True)
    nickname = models.CharField(max_length=30, blank=True, null=True)
    like_count = models.IntegerField()