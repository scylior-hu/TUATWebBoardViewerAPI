# Generated by Django 2.0.3 on 2018-03-21 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('important', models.IntegerField()),
                ('title', models.CharField(max_length=256)),
                ('category', models.CharField(max_length=64)),
                ('administrator', models.CharField(max_length=64)),
                ('body', models.CharField(max_length=4096)),
                ('publisher', models.CharField(max_length=64)),
                ('attach_name', models.CharField(max_length=128)),
                ('attach_url', models.URLField()),
                ('target', models.IntegerField()),
            ],
        ),
    ]