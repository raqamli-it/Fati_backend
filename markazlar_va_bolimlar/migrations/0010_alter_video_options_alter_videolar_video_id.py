# Generated by Django 5.0.6 on 2025-03-02 13:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markazlar_va_bolimlar', '0009_alter_videolar_video_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name': 'Video', 'verbose_name_plural': 'Video'},
        ),
        migrations.AlterField(
            model_name='videolar',
            name='video_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Videolar', to='markazlar_va_bolimlar.video'),
        ),
    ]
