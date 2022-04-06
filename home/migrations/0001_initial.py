# Generated by Django 4.0.3 on 2022-04-06 02:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=128)),
                ('content', models.TextField(blank=True)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]