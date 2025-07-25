from ckeditor.fields import RichTextField
from django.db import models


class Markazlar(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    content_two = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='Markazlar/image', blank=True, null=True)
    file = models.ImageField(upload_to='Bolimlar/image', blank=True, null=True)
    order = models.IntegerField(default=0, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Markazlar'
        verbose_name_plural = 'Markazlar'

    def __str__(self):
        return self.title or 'No title'


class Bolimlar(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    content_two = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='Bolimlar/image', blank=True, null=True)
    file = models.ImageField(upload_to='Bolimlar/image', blank=True, null=True)
    order = models.IntegerField(default=0, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Bo\'limlar'
        verbose_name_plural = 'Bo\'limlar'

    def __str__(self):
        return self.title or 'No title'


class Tadqiqot(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='Tadqiqot/image', blank=True, null=True)
    bolimlar = models.ForeignKey(Bolimlar, on_delete=models.CASCADE, related_name='tadqiqot_bolim', blank=True,
                                 null=True)
    markazlar = models.ForeignKey(Markazlar, on_delete=models.CASCADE, related_name='tadqiqot_markaz', blank=True,
                                  null=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title or 'No title'

    class Meta:
        verbose_name = 'Tadqiqot'
        verbose_name_plural = 'Tadqiqot'


class Xodimlar(models.Model):
    image = models.ImageField(upload_to='Xodimlar/image', blank=True, null=True)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    degree = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    about = RichTextField(blank=True, null=True)
    works = RichTextField(blank=True, null=True)
    bolimlar = models.ForeignKey(Bolimlar, on_delete=models.CASCADE, related_name='xodimlar_bolim', blank=True,
                                 null=True)
    markazlar = models.ForeignKey(Markazlar, on_delete=models.CASCADE, related_name='xodimlar_markaz', blank=True,
                                  null=True)

    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name or 'No full_name'

    class Meta:
        verbose_name = 'Xodim'
        verbose_name_plural = 'Xodimlar'


class Audio(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    audio = models.FileField(upload_to='Audio', blank=True, null=True)
    image = models.ImageField(upload_to='Audio/image', blank=True, null=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Audio'
        verbose_name_plural = 'Audio'


class Audiolar(models.Model):
    audio = models.FileField(upload_to='Audio/audiolar',  blank=True, null=True)
    audio_id = models.ForeignKey(Audio, on_delete=models.CASCADE, related_name='Audiolar', blank=True, null=True)

    class Meta:
        verbose_name = 'Audiolar'
        verbose_name_plural = 'Audiolar'


class Rasm(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='Rasm', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Rasm'
        verbose_name_plural = 'Rasm'


class Rasmlar(models.Model):
    image = models.ImageField(upload_to='Rasm/image', blank=True, null=True)
    image_id = models.ForeignKey(Rasm, on_delete=models.CASCADE, related_name='Rasmlar', blank=True, null=True)

    class Meta:
        verbose_name = 'Rasmlar'
        verbose_name_plural = 'Rasmlar'


class Video(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    video = models.FileField(upload_to='Video', blank=True, null=True)
    image = models.ImageField(upload_to='Video/image', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Video'


class Videolar(models.Model):
    video = models.FileField(upload_to='Video/videos', blank=True, null=True)
    video_id = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='Videolar', blank=True, null=True)

    class Meta:
        verbose_name = 'Videolar'
        verbose_name_plural = 'Videolar'

#
#
# class Photo(models.Model):
#     title = models.CharField(max_length=255, blank=True, null=True)
#     image = models.ImageField(upload_to='media/Photo', blank=True, null=True)
#     bolimlar = models.ForeignKey(Bolimlar, on_delete=models.CASCADE, related_name='photo', blank=True, null=True)
#     markazlar = models.ForeignKey(Markazlar, on_delete=models.CASCADE, related_name='photos', blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         verbose_name = 'Photo'
#         verbose_name_plural = 'Photo'
#
#
# class Video(models.Model):
#     title = models.CharField(max_length=255, blank=True, null=True)
#     video = models.FileField(upload_to='media/Video', blank=True, null=True)
#     link = models.URLField(blank=True, null=True)
#     bolimlar = models.ForeignKey(Bolimlar, on_delete=models.CASCADE, related_name='video', blank=True, null=True)
#     markazlar = models.ForeignKey(Markazlar, on_delete=models.CASCADE, related_name='videos', blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         verbose_name = 'Video'
#         verbose_name_plural = 'Video'
