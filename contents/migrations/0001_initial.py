# Generated by Django 4.0.2 on 2022-02-25 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('post_id', models.CharField(max_length=200)),
                ('comment', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'comments',
            },
        ),
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('post_file', models.FileField(upload_to='uploads/%Y/%m/%d')),
                ('writing', models.TextField(max_length=200)),
                ('postdate', models.DateTimeField(auto_now_add=True)),
                ('like_cnt', models.IntegerField()),
            ],
            options={
                'db_table': 'posts',
            },
        ),
        migrations.CreateModel(
            name='ScrapModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('post_id', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'scraps',
            },
        ),
    ]
