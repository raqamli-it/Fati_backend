# Generated by Django 5.0.6 on 2025-02-14 06:20

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Azolar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('name_uz', models.CharField(max_length=255, null=True)),
                ('name_en', models.CharField(max_length=255, null=True)),
                ('position', models.CharField(max_length=255)),
                ('position_uz', models.CharField(max_length=255, null=True)),
                ('position_en', models.CharField(max_length=255, null=True)),
                ('degree', models.CharField(max_length=255)),
                ('degree_uz', models.CharField(max_length=255, null=True)),
                ('degree_en', models.CharField(max_length=255, null=True)),
                ('contact', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('order', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Azolar',
                'verbose_name_plural': 'Azolar',
            },
        ),
        migrations.CreateModel(
            name='Ilmiy_kengash_majlis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_uz', models.CharField(max_length=255, null=True)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('content_uz', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('content_en', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='images')),
                ('date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Ilmiy kengash majlis',
                'verbose_name_plural': 'Ilmiy kengash majlis',
            },
        ),
        migrations.CreateModel(
            name='Yosh_olimlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_uz', models.CharField(max_length=255, null=True)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('content_uz', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('content_en', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Yosh olim',
                'verbose_name_plural': 'Yosh olimlar',
            },
        ),
    ]
