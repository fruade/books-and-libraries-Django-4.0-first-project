from django.db import models
from django.contrib import admin


class Book(models.Model):
    book_name = models.CharField(max_length=100, verbose_name='Название книги')
    author = models.ManyToManyField('Author', related_name='books', verbose_name='Авторы')
    description = models.TextField(verbose_name='Описание книги', null=True, blank=True)
    id_publishing_house = models.ForeignKey(
        'PublishingHouse',
        on_delete=models.CASCADE,
        related_name='publishinghouse_books',
        verbose_name='ID издательство',
        null=True,
        blank=True
    )
    date_creation = models.DateField(verbose_name='Дата написания книги', null=True, blank=True)
    date_add = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    is_deleted = models.BooleanField(default=False, verbose_name='Удалить')
    book_img = models.ImageField(upload_to='media/%Y/%m/%d',
                                 verbose_name='Ссылка на изображение', blank=True, null=True)

    def __str__(self):
        return self.book_name

    class Meta:
        verbose_name = 'книгу'
        verbose_name_plural = 'Книги'


class PublishingHouse(models.Model):
    publishing_house_name = models.CharField(max_length=300, verbose_name='Название издательства')
    address = models.CharField(max_length=1500, verbose_name='Адрес компании')
    contact_phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Email')
    website_link = models.URLField(verbose_name='Ссылка на сайт', null=True, blank=True)
    date_add = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    is_deleted = models.BooleanField(default=False, verbose_name='Удалить')

    def __str__(self):
        return self.publishing_house_name

    class Meta:
        verbose_name = 'издательство'
        verbose_name_plural = 'Издательства'


class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя автора')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия автора')
    father_name = models.CharField(max_length=100, verbose_name='Отчество автора', null=True, blank=True)
    country = models.CharField(max_length=100, verbose_name='Страна')
    birthday = models.DateField(verbose_name='Дата рождения')
    languages = models.JSONField(verbose_name='Языки на которых писал автор', null=True, blank=True)
    date_add = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    is_deleted = models.BooleanField(default=False, verbose_name='Удалить')

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = 'автора'
        verbose_name_plural = 'Авторы'


class BooksInAuthor(admin.TabularInline):
    model = Book.author.through
