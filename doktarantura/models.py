from ckeditor.fields import RichTextField
from django.db import models


class Qabul_tartibi(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    file = models.FileField(upload_to='Qabul_tartibi/file', blank=True, null=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Qabul tartibi'
        verbose_name_plural = 'Qabul tashkilotlar'


class Malakaviy_imtihon(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    file = models.FileField(upload_to='Malakaviy_imtihon/file', blank=True, null=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Malakaviy imtihon'
        verbose_name_plural = 'Malakaviy imtihonlar'


class Doktarantura(models.Model):
    title = models.CharField(max_length=255)
    labor_activity = RichTextField(blank=True, null=True)
    scientific_activity = RichTextField(blank=True, null=True)
    works = RichTextField(blank=True, null=True)
    file = models.FileField(upload_to='Doktarantura/file', blank=True, null=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Doktarantura'
        verbose_name_plural = 'Doktaranturalar'

