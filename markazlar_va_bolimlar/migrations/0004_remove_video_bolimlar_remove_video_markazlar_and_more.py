# Generated by Django 5.0.9 on 2025-03-01 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('markazlar_va_bolimlar', '0003_alter_xodimlar_activity_alter_xodimlar_activity_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='bolimlar',
        ),
        migrations.RemoveField(
            model_name='video',
            name='markazlar',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]
