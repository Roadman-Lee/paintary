# Generated by Django 4.0 on 2022-03-02 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('image', models.TextField()),
                ('profile_image', models.TextField()),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='email')),
                ('nickname', models.CharField(blank=True, max_length=30, null=True)),
                ('like_count', models.IntegerField()),
            ],
        ),
    ]