# Generated by Django 4.2.1 on 2023-10-26 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_newsitem_created_2ru_api_alter_newsitem_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsitem',
            old_name='created_2ru_api',
            new_name='added_through_api',
        ),
    ]
