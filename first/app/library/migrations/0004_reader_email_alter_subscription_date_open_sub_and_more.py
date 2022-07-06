# Generated by Django 4.0.5 on 2022-06-22 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_library_options_subscription_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='reader',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='date_open_sub',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата открытия'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Удалить'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='number_subscription',
            field=models.CharField(max_length=13, verbose_name='Номер абонемента'),
        ),
    ]
