from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Genres', models.CharField(max_length=255)),
                ('Directed', models.CharField(max_length=255)),
                ('Producers', models.CharField(max_length=255)),
                ('Screenwriters', models.CharField(max_length=255)),
                ('Cinematographer', models.CharField(max_length=255)),
                ('Year', models.IntegerField )
            ],
        ),
    ]
