# Generated by Django 5.1.6 on 2025-03-12 14:18

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='blog_images'),
        ),
    ]
