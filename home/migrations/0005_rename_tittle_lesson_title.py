# Generated by Django 4.0.3 on 2022-04-06 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_lesson_tittle'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='tittle',
            new_name='title',
        ),
    ]