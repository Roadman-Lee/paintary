# Generated by Django 4.0.2 on 2022-02-28 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0003_postmodel_fontstyle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='like_cnt',
            field=models.IntegerField(default=0),
        ),
    ]
