# Generated by Django 3.2.9 on 2021-11-07 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date_of_birth',
            field=models.DateField(blank=True, help_text='Введите дату рождения', null=True, verbose_name='Дата рождения'),
        ),
    ]
