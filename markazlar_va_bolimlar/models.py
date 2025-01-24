from ckeditor.fields import RichTextField
from django.db import models


class Markazlar_Bolimlar(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/image', blank=True, null=True)
    STATUS_CHOICES = [
        ('published', 'Published'),
        ('not_published', 'Not Published'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='published',
        blank=True, null=True,
    )
    order = models.IntegerField(default=0, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Markazlar bo\'limi'
        verbose_name_plural = 'Markazlar bo\'limlari'

    def __str__(self):
        return f'{self.title}'


class Tadqiqot(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/Tadqiqot/', blank=True, null=True)
    center_id = models.ForeignKey(
        Markazlar_Bolimlar,
        on_delete=models.CASCADE,
        related_name='Tadqiqot',
        blank=True,
        null=True
    )
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

    class Meta:
        verbose_name = 'Tadqiqot'
        verbose_name_plural = 'Tadqiqot'


class Xodimlar(models.Model):
    title = models.CharField(max_length=255)
    birth = models.DateField(blank=True, null=True)
    sphere = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    academic_degree = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    image = models.ImageField(upload_to='media/Xodimlar', blank=True, null=True)
    about = RichTextField(blank=True, null=True)
    works = RichTextField(blank=True, null=True)
    batafsil = models.FileField(upload_to='media/Xodimlar/file', blank=True, null=True)
    center_id = models.ForeignKey(
        Markazlar_Bolimlar,
        on_delete=models.CASCADE,
        related_name='xodimlar',
    )

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
        return f'{self.title} ({self.position})'

    class Meta:
        verbose_name = 'Xodimlar'
        verbose_name_plural = 'Xodimlar'


class Photo(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='media/Photo', blank=True, null=True)
    center_id = models.ForeignKey(
        Markazlar_Bolimlar,
        on_delete=models.CASCADE,
        related_name='Photo',
        blank=True,
        null=True
    )
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

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photo'


class Video(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    video = models.FileField(upload_to='media/Video', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    center_id = models.ForeignKey(
        Markazlar_Bolimlar,
        on_delete=models.CASCADE,
        related_name='Video',
        blank=True,
        null=True
    )
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

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Video'
