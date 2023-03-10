# Generated by Django 4.1.6 on 2023-02-13 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h1', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(default='', max_length=255, unique=True, verbose_name='URL')),
                ('description', models.TextField(default='')),
                ('content', models.TextField(default='')),
                ('image', models.ImageField(upload_to='article-images')),
                ('time_created', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=120)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.article')),
            ],
        ),
    ]
