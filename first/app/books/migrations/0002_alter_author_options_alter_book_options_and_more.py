# Generated by Django 4.0.5 on 2022-06-30 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'автора', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'книгу', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterModelOptions(
            name='publishinghouse',
            options={'verbose_name': 'издательство', 'verbose_name_plural': 'Издательства'},
        ),
        migrations.AddField(
            model_name='book',
            name='book_img',
            field=models.ImageField(blank=True, height_field=350, null=True, upload_to='photo/%Y/%m/%d', verbose_name='Ссылка на изображение', width_field=150),
        ),
        migrations.AlterField(
            model_name='author',
            name='country',
            field=models.CharField(max_length=100, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='author',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Удалить'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(related_name='books', to='books.author', verbose_name='Авторы'),
        ),
        migrations.AlterField(
            model_name='book',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Удалить'),
        ),
        migrations.AlterField(
            model_name='publishinghouse',
            name='contact_phone',
            field=models.CharField(max_length=20, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='publishinghouse',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Удалить'),
        ),
    ]
