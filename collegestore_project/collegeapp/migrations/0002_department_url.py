# Generated by Django 4.2.1 on 2023-05-25 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='url',
            field=models.TextField(blank=True),
        ),
    ]
