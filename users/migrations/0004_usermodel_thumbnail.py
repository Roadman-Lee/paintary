# Generated by Django 4.0 on 2022-03-02 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_usermodel_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='thumbnail',
            field=models.CharField(blank=True, default='profile.jpg', max_length=256, null=True),
        ),
    ]
