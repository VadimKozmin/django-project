# Generated by Django 4.0.3 on 2022-06-13 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_сarbonated_carbon_alter_coffee_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='main_menu',
            name='description',
            field=models.TextField(default=1, verbose_name='Описание'),
            preserve_default=False,
        ),
    ]
