# Generated by Django 2.1.2 on 2019-04-19 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0005_migrate_update_dates'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='pinned',
            field=models.BooleanField(default=False),
        ),
    ]
