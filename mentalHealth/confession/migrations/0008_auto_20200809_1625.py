# Generated by Django 2.2 on 2020-08-09 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confession', '0007_post_my_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='my_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='my_video',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
    ]
