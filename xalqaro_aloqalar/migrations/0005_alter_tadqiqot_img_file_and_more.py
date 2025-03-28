# Generated by Django 5.0.9 on 2025-03-01 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xalqaro_aloqalar', '0004_alter_xamkor_loihalar_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tadqiqot',
            name='img_file',
            field=models.ImageField(blank=True, null=True, upload_to='Tadqiqot/images'),
        ),
        migrations.AlterField(
            model_name='xalqaro_sayohatlar',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='Xalqaro_sayohatlar/images'),
        ),
        migrations.AlterField(
            model_name='xamkor_loihalar',
            name='img_file',
            field=models.ImageField(blank=True, null=True, upload_to='Xamkor_loihalar/images'),
        ),
        migrations.AlterField(
            model_name='xamkor_tashkilot',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='Xamkor_tashkilot/images'),
        ),
    ]
