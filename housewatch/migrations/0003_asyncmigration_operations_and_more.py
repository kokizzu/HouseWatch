# Generated by Django 4.1.1 on 2023-03-29 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housewatch', '0002_asyncmigration_asyncmigration_unique name'),
    ]

    operations = [
        migrations.AddField(
            model_name='asyncmigration',
            name='operations',
            field=models.JSONField(default=[]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='asyncmigration',
            name='rollback_operations',
            field=models.JSONField(blank=True, null=True),
        ),
    ]