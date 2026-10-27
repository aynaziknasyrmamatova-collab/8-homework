from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Shop(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shops',
        null=True,
        blank=True,
        verbose_name='Владелец'
    )
    name = models.CharField(max_length=60, verbose_name='Название')
    color = models.CharField(max_length=30, verbose_name='Цвет')
    logo = models.ImageField(upload_to='logo/', blank=True, null=True, verbose_name='Логотип')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'


class Product(models.Model):
    shop = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Магазин',
    )
    name = models.CharField(max_length=120, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
