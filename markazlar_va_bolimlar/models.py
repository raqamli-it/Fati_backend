from ckeditor.fields import RichTextField
from django.db import models


class Markazlar(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/Markazlar', blank=True, null=True)
    order = models.IntegerField(default=0, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Markazlar'
        verbose_name_plural = 'Markazlar'

    def __str__(self):
        return f'{self.title}'


class Bolimlar(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/Bolimlar', blank=True, null=True)
    order = models.IntegerField(default=0, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Bo\'limlar'
        verbose_name_plural = 'Bo\'limlar'

    def __str__(self):
        return f'{self.title}'


class Tadqiqot(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/Tadqiqot/', blank=True, null=True)
    bolimlar = models.ForeignKey(Bolimlar, on_delete=models.CASCADE, related_name='tadqiqot', blank=True, null=True)
    markazlar = models.ForeignKey(Markazlar, on_delete=models.CASCADE, related_name='tadqiqotlar', blank=True,
                                  null=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tadqiqot'
        verbose_name_plural = 'Tadqiqot'


class Xodimlar(models.Model):
    image = models.ImageField(upload_to='media/Xodimlar', blank=True, null=True)
    ful_name = models.CharField(max_length=50)
    activity = models.TextField(max_length=1000, blank=True, null=True)
    about = RichTextField(blank=True, null=True)
    works = RichTextField(blank=True, null=True)
    bolimlar = models.ForeignKey(Bolimlar, on_delete=models.CASCADE, related_name='xodimlar', blank=True, null=True)
    markazlar = models.ForeignKey(Markazlar, on_delete=models.CASCADE, related_name='xodim', blank=True, null=True)
    file = models.FileField(upload_to='xodimlar/file', blank=True, null=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ful_name

    class Meta:
        verbose_name = 'Xodim'
        verbose_name_plural = 'Xodimlar'


class Photo(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='media/Photo', blank=True, null=True)
    bolimlar = models.ForeignKey(Bolimlar, on_delete=models.CASCADE, related_name='photo', blank=True, null=True)
    markazlar = models.ForeignKey(Markazlar, on_delete=models.CASCADE, related_name='photos', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photo'


class Video(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    video = models.FileField(upload_to='media/Video', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    bolimlar = models.ForeignKey(Bolimlar, on_delete=models.CASCADE, related_name='video', blank=True, null=True)
    markazlar = models.ForeignKey(Markazlar, on_delete=models.CASCADE, related_name='videos', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Video'
