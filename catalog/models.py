from typing import Optional

from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}

class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='products/', **NULLABLE)

    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория', null=True)

    price = models.IntegerField(verbose_name='цена за штуку')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='дата обновления')
    is_published = models.BooleanField(default=False, verbose_name='опубликовано')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='продавец')

    def __str__(self):
        return f'{self.category} {self.name} {self.price}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('price',)




class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='название')
    category_description = models.TextField(verbose_name='описание', **NULLABLE)
    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('category_name',)


class Version(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    number = models.IntegerField(verbose_name='номер версии')
    title = models.CharField(max_length=100, verbose_name='нахвание версии')
    current = models.BooleanField(default=False, verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.product_name} {self.current}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'