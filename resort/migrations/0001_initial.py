# Generated by Django 4.0.3 on 2022-03-07 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Hero_Images/', verbose_name='Upload Image for Hero Section')),
                ('name', models.CharField(blank=True, default='RESORT NAME', max_length=100, null=True, verbose_name='Set a Cool Name of ReSort')),
                ('tag', models.CharField(blank=True, default='STAY WITH FRIENDS & FAMILIES', max_length=100, null=True, verbose_name='Set a Tagline for Hero Section')),
                ('greet', models.CharField(blank=True, default='GET ACCOMMODATION TODAY', max_length=100, null=True, verbose_name='Set a Greeting for Hero Section')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Hero Section',
                'verbose_name_plural': 'Hero Section',
            },
        ),
    ]
