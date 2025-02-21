from ckeditor.fields import RichTextField
from django.db import models


class Xamkor_tashkilot(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    file = models.FileField(upload_to='images', blank=True, null=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Xamkor tashkilot'
        verbose_name_plural = 'Xamkor tashkilotlar'


class Xamkor_loihalar(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    img_file = models.ImageField(upload_to='images', blank=True, null=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = [
        ('Bajarilgan loyihalar', 'Bajarilgan loyihalar'),
        ('Amaldagi loyihalar', 'Amaldagi loyihalar'),
    ]
    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='Amaldagi loyihalar',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Xamkor loiha'
        verbose_name_plural = 'Xamkor loihalar'


class Xalqaro_sayohatlar(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    subcontent = RichTextField(blank=True, null=True)
    file = models.FileField(upload_to='images', blank=True, null=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ilmiy safarlar'
        verbose_name_plural = 'Ilmiy safarlar'


class Tadqiqot(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    img_file = models.ImageField(upload_to='images', blank=True, null=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tadqiqot'
        verbose_name_plural = 'Tadqiqot'
