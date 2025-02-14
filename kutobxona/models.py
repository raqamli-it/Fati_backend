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
    position = models.CharField(max_length=255, blank=True, null=True)
    degree = models.CharField(max_length=255, blank=True, null=True)
    sphere = models.CharField(max_length=255, blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    file = models.FileField(upload_to='media/tahririyat', blank=True, null=True)
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


class Period(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Period books'
        verbose_name_plural = 'Period books'


class Books(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='Books/image', blank=True, null=True)
    file = models.FileField(blank=True, null=True)
    period = models.ManyToManyField(Period, related_name='books')
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class Comment(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='Comment/file', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class Period_filter(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'arxiv hujjat filter'
        verbose_name_plural = 'arxiv hujjat filter'


class archive_documents(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='archive/image', blank=True, null=True)
    file = models.FileField(blank=True, null=True)
    period_filter = models.ManyToManyField(Period_filter, related_name='documents')
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'arxiv hujjat'
        verbose_name_plural = 'arxiv hujjatlar'


class Abstract(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='media/Avtoreferat/image', blank=True, null=True)
    file = models.FileField(upload_to='media/Avtoreferat/file/', blank=True, null=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Disertatsiya va avtorefarat'
        verbose_name_plural = 'Disertatsiya va avtorefaratlar'


class Mat_category(models.Model):
    title = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Mat category'
        verbose_name_plural = 'Mat category'


class Year_filter(models.Model):
    title = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Year filter'
        verbose_name_plural = 'Year filter'


class Region_filter(models.Model):
    title = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Region filter'
        verbose_name_plural = 'Region filter'


class the_press(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='matbuot/image', blank=True, null=True)
    file = models.FileField(upload_to='matbuot/file', blank=True, null=True)
    mat_cotegory = models.ForeignKey(Mat_category, on_delete=models.SET_NULL, null=True, related_name='cotegory')
    year_id = models.ManyToManyField(Year_filter, related_name='year', )
    region_id = models.ForeignKey(Region_filter, on_delete=models.SET_NULL, null=True, related_name='region', )
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Matbuot'
        verbose_name_plural = 'Matbuotlar'
