# Generated by Django 4.0.2 on 2022-03-01 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0006_alter_postmodel_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='like_cnt',
        ),
    ]
