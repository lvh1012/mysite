# Generated by Django 4.0.3 on 2022-04-07 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_tittle_lesson_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='summary',
            field=models.CharField(default='1', max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lesson',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
