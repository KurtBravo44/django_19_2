from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='products/', **NULLABLE)

    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория', null=True)

    price = models.IntegerField(verbose_name='цена за штуку')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='дата обновления')

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

