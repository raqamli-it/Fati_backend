from ckeditor.fields import RichTextField
from django.db import models


class MarkazlarBolimlar(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    tarix = RichTextField(blank=True, null=True)
    STATUS_CHOICES = [
        ('published', 'Published'),
        ('not_published', 'Not Published'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='published', blank=True, null=True,
    )
    order = models.IntegerField(default=0, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Markazlar bo\'limi'
        verbose_name_plural = 'Markazlar bo\'limlari'

    def __str__(self):
        return f'{self.title}'

    def get_barcha_rasmlar(self):
        return self.rasmlar.all()


class Rasmlar(models.Model):
    fotogalereya = models.ImageField(upload_to='images', max_length=255, blank=True, null=True)
    silder = models.ImageField(upload_to='images', max_length=255, blank=True, null=True)
    markazlar_bolimlar = models.ForeignKey(
        MarkazlarBolimlar,
        on_delete=models.CASCADE,
        related_name='rasmlar',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Rasmlar'
        verbose_name_plural = 'Rasmlar'


class Xodimlar(models.Model):
    name = models.CharField(max_length=255)
    lavozim = models.CharField(max_length=255)
    ilmiy_daraja = models.CharField(max_length=255)

    # ForeignKey to'g'rilangan
    markazlar_bolimlar = models.ForeignKey(
        MarkazlarBolimlar,
        on_delete=models.CASCADE,
        related_name='xodimlar',
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

    def __str__(self):
        return f'{self.name} ({self.lavozim})'

    class Meta:
        verbose_name = 'Xodim'
        verbose_name_plural = 'Xodimlar'
