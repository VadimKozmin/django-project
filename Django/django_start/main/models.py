from django.db import models


class Main_menu(models.Model):
    title = models.CharField('Название', max_length=50)
    count = models.IntegerField('Цена')
    description = models.TextField('Описание', default=' ')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Закуски'
        verbose_name_plural = 'Закуски'


class Salad(models.Model):
    title = models.CharField('Название', max_length=50)
    count = models.IntegerField('Цена')
    description = models.TextField('Описание', default=' ')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Салаты'
        verbose_name_plural = 'Салаты'


class Rus(models.Model):
    title = models.CharField('Название', max_length=50)
    count = models.IntegerField('Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'А-ля русс'
        verbose_name_plural = 'А-ля русс'


class Main(models.Model):
    title = models.CharField('Название', max_length=50)
    count = models.IntegerField('Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Основное'
        verbose_name_plural = 'Основное'


class Dessert(models.Model):
    title = models.CharField('Название', max_length=50)
    count = models.IntegerField('Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Десерт'
        verbose_name_plural = 'Десерт'


class Coffee(models.Model):
    title = models.CharField('Название', max_length=50)
    count = models.IntegerField('Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кофе'
        verbose_name_plural = 'Кофе'


class Tea(models.Model):
    title = models.CharField('Название', max_length=50)
    count = models.IntegerField('Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Чай'
        verbose_name_plural = 'Чай'


class Water(models.Model):
    title = models.CharField('Название', max_length=50)
    count = models.IntegerField('Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вода'
        verbose_name_plural = 'Вода'


class Juice(models.Model):
    title = models.CharField('Название', max_length=50)
    count = models.IntegerField('Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Соки'
        verbose_name_plural = 'Соки'


class Carbon(models.Model):
    title = models.CharField('Название', max_length=50)
    count = models.IntegerField('Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Газированные напитки'
        verbose_name_plural = 'Газированные напитки'


class Author(models.Model):
    title = models.CharField('Название', max_length=50)
    count = models.IntegerField('Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Авторские напитки'
        verbose_name_plural = 'Авторские напитки'


class Author_drinks(models.Model):
    title = models.CharField('Название', max_length=50)
    count = models.IntegerField('Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Напитки собственного производства'
        verbose_name_plural = 'Напитки собственного производства'


class Coctails(models.Model):
    title = models.CharField('Название', max_length=50)
    count = models.IntegerField('Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Коктейли безалкогольные'
        verbose_name_plural = 'Коктейли безалкогольные'


class Soup(models.Model):
    title = models.CharField('Название', max_length=50)
    count = models.IntegerField('Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Супы'
        verbose_name_plural = 'Супы'


