from unicodedata import category
from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from faker import Faker
fake = Faker()
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False, verbose_name='Наименование')
    image = models.ImageField(verbose_name='Фото', upload_to='images/category/', null=True, blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории' 


class Games(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255, null=True, blank=True)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2, null=True, blank=True,validators=[MinValueValidator(0)])
    image = models.ImageField(verbose_name='Фото', upload_to='images/products/', null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL , null=True, blank=True)
    key = models.CharField(verbose_name='ключ', default=fake.bothify(text='?????-?????-?????-?????'), max_length=50, null=True, blank=True)
    
    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры' 



class Order(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    games = models.ForeignKey(Games, verbose_name='Игра', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона', null=True, blank=True)
  
    
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

  
    
    def __str__(self):
        return f'Заказ №{self.id} ({self.user})'


    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы' 

