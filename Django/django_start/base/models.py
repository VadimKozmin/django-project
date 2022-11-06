from django.db import models


class Soup(models.Model):
    title1 = models.CharField('Название', max_length=50)

    def __str__(self):
        return self.title1

    class Meta:
        verbose_name = 'Супы (комплексный обед)'
        verbose_name_plural = 'Супы (комплексный обед)'


class Second_dish(models.Model):
    title_second_dish = models.CharField('Название', max_length=50)

    def __str__(self):
        return self.title_second_dish

    class Meta:
        verbose_name = 'Вторые блюда (комплексный обед)'
        verbose_name_plural = 'Вторые блюда (комплексный обед)'


class Salad(models.Model):
    title_salad = models.CharField('Название', max_length=50)

    def __str__(self):
        return self.title_salad

    class Meta:
        verbose_name = 'Салат (комплексный обед)'
        verbose_name_plural = 'Салаты (комплексный обед)'


class Drinks(models.Model):
    title_drinks = models.CharField('Название', max_length=50)

    def __str__(self):
        return self.title_drinks

    class Meta:
        verbose_name = 'Напиток (комплексный обед)'
        verbose_name_plural = 'Напитки (комплексный обед)'








