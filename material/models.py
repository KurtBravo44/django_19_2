from django.db import models

from catalog.models import NULLABLE


class Material(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    body = models.TextField(verbose_name='содержимое')

    time_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания', null=True, blank=True)
    image = models.ImageField(upload_to='materials/', **NULLABLE)
    views_count = models.IntegerField(default=0, verbose_name='просмотры')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    slug = models.CharField(max_length=100, verbose_name='slug', null=True, blank=True)

    def __str__(self):
        return self.title



    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'

