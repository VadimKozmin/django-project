# Generated by Django 4.0.3 on 2022-06-13 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_main_menu_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_menu',
            name='description',
            field=models.TextField(default='', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='salad',
            name='description',
            field=models.TextField(default='', verbose_name='Описание'),
        ),
    ]
