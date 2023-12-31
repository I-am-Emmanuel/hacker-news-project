# Generated by Django 4.2.1 on 2023-10-25 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('url', models.URLField()),
                ('points', models.PositiveIntegerField(default=0)),
                ('author', models.CharField(max_length=15)),
                ('comments', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
