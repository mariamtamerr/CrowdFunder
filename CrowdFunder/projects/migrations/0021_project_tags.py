# Generated by Django 4.2.6 on 2023-10-23 12:05

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0020_alter_project_category_alter_project_end_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.TextField(),
        ),
    ]
