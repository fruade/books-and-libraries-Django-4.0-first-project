# Generated by Django 4.0.5 on 2022-06-22 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='library',
            options={'verbose_name': 'Библиотеку', 'verbose_name_plural': 'Библиотеки'},
        ),
        migrations.AddField(
            model_name='subscription',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Удалено'),
        ),
    ]
