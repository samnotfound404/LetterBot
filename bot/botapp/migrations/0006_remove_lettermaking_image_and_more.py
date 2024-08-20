# Generated by Django 4.2.15 on 2024-08-20 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botapp', '0005_remove_lettermaking_photo_lettermaking_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lettermaking',
            name='Image',
        ),
        migrations.AddField(
            model_name='lettermaking',
            name='CompanyAddress',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lettermaking',
            name='CompanyEmail',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='lettermaking',
            name='CompanyName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='lettermaking',
            name='CompanyPhone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
