# Generated by Django 4.0.3 on 2022-04-12 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_tag_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=1024)),
                ('thumbnail', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
