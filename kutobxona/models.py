
from ckeditor.fields import RichTextField
from django.db import models


class Talablar(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    sub_content = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/talablar', blank=True, null=True)
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
    Updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Talab'
        verbose_name_plural = 'Talablar'


class Tahririyat(models.Model):
    title = models.CharField(max_length=255)
    position = models.CharField(max_length=255, blank=True, null=True)
    degree = models.CharField(max_length=255, blank=True, null=True)
    sphere = models.CharField(max_length=255, blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    file = models.FileField(upload_to='media/tahririyat', blank=True, null=True)
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
    Updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tahririyat'
        verbose_name_plural = 'Tahririyat'


class Category(models.Model):
    title = models.CharField(max_length=255)
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
        verbose_name = 'Categoriya'
        verbose_name_plural = 'Categoriyalar'


class Avtoreferat(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/Avtoreferat/image', blank=True, null=True)
    file = models.FileField(upload_to='media/Avtoreferat/file/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Avtoreferat', blank=True, null=True)
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
    Updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Disertatsiya va avtorefarat'
        verbose_name_plural = 'Disertatsiya va avtorefaratlar'


class Arxiv(models.Model):
    title = models.CharField(max_length=255, null=True)
    content = RichTextField(blank=True, null=True)
    sub_content = RichTextField(blank=True, null=True)
    image = models.FileField(upload_to='media/Arxiv/image', blank=True, null=True)
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
    Updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Arxiv'
        verbose_name_plural = 'Arxivlar'