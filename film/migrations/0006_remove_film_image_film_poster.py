# Generated by Django 5.1.4 on 2025-01-15 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0005_remove_film_cinematographer_remove_film_producers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='image',
        ),
        migrations.AddField(
            model_name='film',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
