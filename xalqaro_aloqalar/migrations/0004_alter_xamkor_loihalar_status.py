# Generated by Django 5.0.6 on 2025-02-21 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xalqaro_aloqalar', '0003_alter_xamkor_loihalar_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xamkor_loihalar',
            name='status',
            field=models.CharField(choices=[('Bajarilgan loyihalar', 'Bajarilgan loyihalar'), ('Amaldagi loyihalar', 'Amaldagi loyihalar')], default='Amaldagi loyihalar', max_length=30),
        ),
    ]
