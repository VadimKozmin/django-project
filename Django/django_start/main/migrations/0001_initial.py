# Generated by Django 4.0.3 on 2022-06-13 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Main_menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('count', models.IntegerField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Основное меню',
                'verbose_name_plural': 'Основное меню',
            },
        ),
    ]
