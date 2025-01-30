from ckeditor.fields import RichTextField
from django.db import models


class Ilmiy_kengash_majlis(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    file = models.FileField(upload_to='images', blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    STATUS_CHOICES = [
        ('published', 'Published'),
        ('not_published', 'Not Published'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='published',
    )
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ilmiy kengash majlis'
        verbose_name_plural = 'Ilmiy kengash majlis'


class Yosh_olimlar(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    file = models.FileField(upload_to='images', blank=True, null=True)
    STATUS_CHOICES = [
        ('published', 'Published'),
        ('not_published', 'Not Published'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='published',
    )
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Yosh olim'
        verbose_name_plural = 'Yosh olimlar'


class Azolar(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    STATUS_CHOICES = [
        ('published', 'Published'),
        ('not_published', 'Not Published'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='published',
    )
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Azolar'
        verbose_name_plural = 'Azolar'

