from ckeditor.fields import RichTextField
from django.db import models


class Requirements(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    sub_content = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/talablar', blank=True, null=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Talab'
        verbose_name_plural = 'Talablar'


class Editorial(models.Model):
    title = models.CharField(max_length=255, null=True)
    content = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/tahririyat', blank=True, null=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tahririyat'
        verbose_name_plural = 'Tahririyat'


class Archive(models.Model):
    title = models.CharField(max_length=255, null=True)
    year = models.CharField(max_length=255, blank=True, null=True)
    image = models.FileField(upload_to='media/Arxiv/image', blank=True, null=True)
    file = models.FileField(blank=True, null=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Arxiv'
        verbose_name_plural = 'Arxivlar'


class Sources(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='Manbalar/image', blank=True, null=True)
    file = models.FileField(blank=True, null=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Manbalar'
        verbose_name_plural = 'Manbalar'
#


class Literature(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='Adabiyot/image', blank=True, null=True)
    file = models.FileField(blank=True, null=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Adabiyot'
        verbose_name_plural = 'Adabiyotlar'


class Abstract(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='media/Avtoreferat/image', blank=True, null=True)
    file = models.FileField(upload_to='media/Avtoreferat/file/', blank=True, null=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Avtorefarat'
        verbose_name_plural = 'Avtorefaratlar'
