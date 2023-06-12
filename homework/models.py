import uuid

from django.db import models

# Create your models here.

'''
class Student(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='имя')
    last_name = models.CharField(max_length=20, verbose_name='фамилия')
    is_active = models.BooleanField(default=True, verbose_name='учится')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'

'''


class Product(models.Model):
    name_product = models.CharField(max_length=20, verbose_name='имя')
    description = models.CharField(max_length=150, verbose_name='описание')
    preview = models.ImageField(verbose_name='изображение', null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    price = models.IntegerField(verbose_name='цена')
    made = models.DateField(verbose_name='изготовлено')
    change = models.DateField(verbose_name='изменено', null=True)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.pk} {self.name_product} {self.price} {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    name_category = models.CharField(max_length=20, verbose_name='имя')
    description = models.CharField(max_length=150, verbose_name='описание')

    def __str__(self):
        return f'{self.pk} {self.name_category}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'