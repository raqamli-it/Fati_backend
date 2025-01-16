from ckeditor.fields import RichTextField
from django.db import models


class Xamkor_tashkilot(models.Model):
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
        verbose_name = 'Xamkor tashkilot'
        verbose_name_plural = 'Xamkor tashkilotlar'


class Xamkor_loihalar(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    img_file = models.ImageField(upload_to='images', blank=True, null=True)
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
        verbose_name = 'Xamkor loiha'
        verbose_name_plural = 'Xamkor loihalar'


class Xalqaro_sayohatlar(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    subcontent = RichTextField(blank=True, null=True)
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
        verbose_name = 'Xalqaro sayohat'
        verbose_name_plural = 'Xalqaro sayohatlar'


class Kelganlar(models.Model):
    kelgan_yil = models.CharField(max_length=255)
    ism = models.CharField(max_length=255)
    ish_joy = models.CharField(max_length=255)
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
        return f"{self.ism} - {self.kelgan_yil}"

    class Meta:
        verbose_name = 'Kelganlar'
        verbose_name_plural = 'Kelganlar'


class Tadqiqot(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    img_file = models.ImageField(upload_to='images', blank=True, null=True)
    kelganlar = models.ForeignKey(Kelganlar, on_delete=models.CASCADE, related_name='kelganlarlar',)

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
        verbose_name = 'Tadqiqot'
        verbose_name_plural = 'Tadqiqot'


