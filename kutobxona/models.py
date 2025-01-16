
from ckeditor.fields import RichTextField
from django.db import models


class Talablar(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    img_url = models.ImageField(upload_to='images', blank=True, null=True)
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


class Tahrirchi(models.Model):
    title = models.CharField(max_length=255)
    ish_joyi = models.CharField(max_length=255)
    lavozimi = models.CharField(max_length=255)
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


class Avtoreferat(models.Model):
    title = models.CharField(max_length=255)
    cover_img = models.ImageField(upload_to='images', blank=True, null=True)
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
    Updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Avtoreferat'
        verbose_name_plural = 'Avtoreferat'


class ElektronKitob(models.Model):
    title = models.CharField(max_length=255)
    cover_img = models.ImageField(upload_to='images', blank=True, null=True)
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
    Updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Elektron Kitob'
        verbose_name_plural = 'Elektron Kitob'


class Manba(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    cover_img = models.ImageField(upload_to='images', blank=True, null=True)
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
    Updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Manbalar'
        verbose_name_plural = 'Manbalar'


class Arxiv(models.Model):
    title = models.CharField(max_length=255, null=True)
    yil = models.CharField(max_length=255, blank=True, null=True)
    nashr_raqami = models.CharField(max_length=255, blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    image = models.FileField(upload_to='image', blank=True, null=True)
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


# class Arxiv(models.Model):
#     yil = models.CharField(max_length=255, blank=True, null=True)
#     nashr_raqami = models.CharField(max_length=255, blank=True, null=True)
#     arxiv_menu = models.ForeignKey(ArxivMenu, on_delete=models.CASCADE, related_name='arxiv_menu',)
#
#     STATUS_CHOICES = [
#         ('published', 'Published'),
#         ('not_published', 'Not Published'),
#     ]
#     status = models.CharField(
#         max_length=20,
#         choices=STATUS_CHOICES,
#         default='published',
#     )
#
#     order = models.IntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     Updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return f"{self.yil} - {self.nashr_raqami}"
#
#     class Meta:
#         verbose_name = 'Arxiv'
#         verbose_name_plural = 'Arxivlar'
