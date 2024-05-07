from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class DishCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255)
    is_visible = models.BooleanField(default=True)
    sort = models.PositiveIntegerField()

    def __iter__(self):
        for item in self.dishes.filter(is_visible=True):
            yield item

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорія страв'
        verbose_name_plural = 'Категорії страв'
        ordering = ['-sort']

class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True)
    ingredients = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_visible = models.BooleanField(default=True)
    category = models.ForeignKey(DishCategory, on_delete=models.CASCADE, related_name='dishes')
    sort = models.PositiveIntegerField()

    photo = models.ImageField(upload_to='dishes/', blank=True, null=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Страва'
        verbose_name_plural = 'Страви'
        ordering = ['sort']



class Events(models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_visible = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    photo = models.ImageField(upload_to='events/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подія'
        verbose_name_plural = 'Події'
        ordering = ['name']


class Chefs(models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_visible = models.BooleanField(default=True)
    position = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='chefs/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Кухар'
        verbose_name_plural = 'Кухари'
        ordering = ['name']


class Gallery(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
        ordering = ['name']


class Contacts(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. "
                                         "Up to 15 digits allowed.")

    address = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=20, validators=[phone_regex])
    time = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return f'{self.phone}, {self.address}, {self.email}, {self.time}'

    class Meta:
        verbose_name = 'Контакти'
        verbose_name_plural = 'Контакти'








