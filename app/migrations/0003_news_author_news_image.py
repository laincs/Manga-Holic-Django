# Generated by Django 4.2.3 on 2024-01-17 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='author',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news_images/'),
        ),
    ]