# Generated by Django 4.2.7 on 2025-01-20 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('roll', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('fathers_name', models.CharField(max_length=20)),
                ('address', models.TextField()),
            ],
        ),
    ]
