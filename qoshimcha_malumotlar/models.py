from django.db import models
from ckeditor.fields import RichTextField


class Institut_tarixi(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='Institut_tarixi/images', blank=True, null=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Institut tarixi'
        verbose_name_plural = 'Institut tarixi'


class Xodimlar_turlari(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Xodimlar turlari'
        verbose_name_plural = 'Xodimlar turlari'


class Xodimlar(models.Model):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    year = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='Xodimlar/image', blank=True, null=True)
    category = models.ForeignKey(Xodimlar_turlari, on_delete=models.CASCADE, related_name='Xodimlar', blank=True)

    class Meta:
        verbose_name = 'Xodimlar'
        verbose_name_plural = 'Xodimlar'


class Aloqa(models.Model):
    phone = models.CharField(max_length=255, verbose_name='Telefon', blank=True, null=True)
    email = models.EmailField(blank=True, null=True, verbose_name='Email')
    adress = models.CharField(max_length=255, verbose_name='Manzil', blank=True, null=True)
    lat = models.FloatField(blank=True, null=True, verbose_name='Latitude')
    long = models.FloatField(blank=True, null=True, verbose_name='Longitude')
    youtube = models.CharField(max_length=255, verbose_name='Youtube', blank=True, null=True)
    telegram = models.CharField(max_length=255, verbose_name='Telegram', blank=True, null=True)
    instagram = models.CharField(max_length=255, verbose_name='Instagram', blank=True, null=True)
    facebook = models.CharField(max_length=255, verbose_name='Facebook', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = 'Aloqa'
        verbose_name_plural = 'Aloqalar'


class Xabarlar(models.Model):
    name = models.CharField(max_length=255, verbose_name='Ism')
    phone = models.CharField(max_length=255, verbose_name='Telefon')
    content = models.TextField(verbose_name='Xabar')

    def __str__(self):
        return f"{self.name} - {self.phone}"

    class Meta:
        verbose_name = 'Xabarlar'
        verbose_name_plural = 'Xabarlar'


class Karusel(models.Model):
    file = models.ImageField(upload_to='Karusel/images', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = 'Karusel'
        verbose_name_plural = 'Karusel'


class Rahbariyat(models.Model):
    title = models.CharField(max_length=255)
    position = models.CharField(max_length=255, blank=True, null=True)
    degree = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    days = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='Rahbariyat/images', blank=True, null=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Rahbariyat'
        verbose_name_plural = 'Rahbariyat'


class Tashkiliy_tuzulma(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    file = models.ImageField(upload_to='Tashkiliy_tuzulma/images', blank=True, null=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tashkiliy tuzulma'
        verbose_name_plural = 'Tashkiliy tuzulma'


class Yangiliklar(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='Yangiliklar/images', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'


class Havolalar(models.Model):
    title = models.CharField(max_length=255)
    file = models.ImageField(upload_to='Havolalar/images', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Havola'
        verbose_name_plural = 'Havolalar'


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'


class Kadirlar_bolim(models.Model):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='Kadirlar/image', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='kadirlar', blank=True)

    class Meta:
        verbose_name = 'Kadirlar bolimi'
        verbose_name_plural = 'Kadirlar bolimi'
