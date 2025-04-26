from ckeditor.fields import RichTextField
from django.db import models


class Ilmiy_kengash_majlis(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title if self.title else "No title"

    class Meta:
        verbose_name = 'Instut ilmiy kengash'
        verbose_name_plural = 'Instut ilmiy kengash'


class Xodimlar(models.Model):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='Xodimlar',  blank=True, null=True)
    center_id = models.ForeignKey(Ilmiy_kengash_majlis, related_name='xodimlar', on_delete=models.CASCADE, blank=True,
                                  null=True)

    class Meta:
        verbose_name = 'Xodimlar'
        verbose_name_plural = 'Xodimlar'


class Content(models.Model):
    content = RichTextField(blank=True, null=True)
    center_id = models.ForeignKey(Ilmiy_kengash_majlis, on_delete=models.CASCADE, related_name='content_id',
                                  blank=True, null=True)


class Yosh_olimlar(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    file = models.FileField(upload_to='Yosh_olimlar/images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title or 'NO title'

    class Meta:
        verbose_name = 'Yosh olim'
        verbose_name_plural = 'Yosh olimlar'

class YoshXodim(models.Model):
    yosh_olim = models.ForeignKey(Yosh_olimlar, on_delete=models.CASCADE, related_name='yosh_xodimlar')
    fullname = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Xodimlar/images/', blank=True, null=True)

    def __str__(self):
        return self.fullname
 
class Azolar(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title or 'No title'

    class Meta:
        verbose_name = 'Ilmiy daraja beruchi kengash'
        verbose_name_plural = 'Ilmiy daraja beruchi kengash'


class Kadirlar(models.Model):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='Kadirlar', blank=True, null=True)
    workplace = models.CharField(max_length=255, blank=True, null=True)
    shifri = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    degree = models.CharField(max_length=255, blank=True, null=True)
    academic_title = models.CharField(max_length=255, blank=True, null=True)
    center_id = models.ForeignKey(Azolar, on_delete=models.CASCADE, related_name='kadirlar', blank=True, null=True)

    class Meta:
        verbose_name = 'Kadirlar'
        verbose_name_plural = 'Kadirlar'


class Text(models.Model):
    content = RichTextField(blank=True, null=True)
    center_id = models.ForeignKey(Azolar, on_delete=models.CASCADE, related_name='text_id',
    blank=True, null=True)

   


class Elonlar(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='Elonlar/image', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title or "No title"
   

    class Meta:
        verbose_name = 'Elonlar'
        verbose_name_plural = 'Elonlar'
