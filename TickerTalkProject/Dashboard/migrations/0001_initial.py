# Generated by Django 4.2.5 on 2023-09-19 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommentsTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=250)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
    ]
