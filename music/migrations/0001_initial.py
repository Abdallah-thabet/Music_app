# Generated by Django 3.1.1 on 2020-09-23 09:41

from django.db import migrations, models
import django.db.models.deletion
import music.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('singer', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=20)),
                ('logo', models.ImageField(blank=True, null=True, upload_to=music.models.store_image)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('file_type', models.CharField(max_length=20)),
                ('file', models.FileField(blank=True, null=True, upload_to=music.models.mp3)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.album')),
            ],
        ),
    ]
