# Generated by Django 5.0.6 on 2025-02-27 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kengashlar', '0002_elonlar_rename_contact_azolar_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='azolar',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='azolar',
            name='title_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='azolar',
            name='title_uz',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='elonlar',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='elonlar',
            name='title_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='elonlar',
            name='title_uz',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ilmiy_kengash_majlis',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ilmiy_kengash_majlis',
            name='title_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ilmiy_kengash_majlis',
            name='title_uz',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
