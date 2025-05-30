# Generated by Django 5.0.9 on 2025-03-07 06:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kengashlar', '0005_alter_yosh_olimlar_file'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='azolar',
            options={'verbose_name': 'Ilmiy daraja beruchi kengash', 'verbose_name_plural': 'Ilmiy daraja beruchi kengash'},
        ),
        migrations.AlterModelOptions(
            name='ilmiy_kengash_majlis',
            options={'verbose_name': 'Instut ilmiy kengash', 'verbose_name_plural': 'Instut ilmiy kengash'},
        ),
        migrations.CreateModel(
            name='Kadirlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Kadirlar')),
                ('position', models.CharField(blank=True, max_length=255, null=True)),
                ('degree', models.CharField(blank=True, max_length=255, null=True)),
                ('academic_title', models.CharField(blank=True, max_length=255, null=True)),
                ('center_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kadirlar', to='kengashlar.azolar')),
            ],
        ),
        migrations.CreateModel(
            name='Xodimlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Xodimlar')),
                ('center_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kengashlar.ilmiy_kengash_majlis')),
            ],
        ),
    ]
