from ckeditor.fields import RichTextField
from django.db import models


class Seminar_turlari(models.Model):
    title = models.CharField(max_length=255)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Seminar turi'
        verbose_name_plural = 'Seminar turlari'


class Seminar(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    seminar_id = models.ForeignKey(Seminar_turlari, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Seminar'
        verbose_name_plural = 'Seminarlar'
