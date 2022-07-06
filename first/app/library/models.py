from django.db import models


class Library(models.Model):
    library_name = models.CharField(max_length=100, verbose_name='Название библиотеки')
    address = models.CharField(max_length=1500, verbose_name='Адрес библиотеки')
    readers = models.ManyToManyField('Reader', related_name='readers_library', verbose_name='Читатели', blank=True)
    contact_phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    website_link = models.URLField(verbose_name='Ссылка на сайт', null=True, blank=True)
    date_add = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    is_deleted = models.BooleanField(default=False, verbose_name='Удалить')

    def __str__(self):
        return self.library_name

    class Meta:
        verbose_name = 'библиотеку'
        verbose_name_plural = 'Библиотеки'


class Reader(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    father_name = models.CharField(max_length=100, verbose_name='Отчество', null=True, blank=True)
    birthday = models.DateField(verbose_name='Дата рождения')
    contact_phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Email', null=True, blank=True)
    date_add = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    is_deleted = models.BooleanField(default=False, verbose_name='Удалено')

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = 'читателя'
        verbose_name_plural = 'Читатели'


class Subscription(models.Model):
    number_subscription = models.CharField(max_length=13, verbose_name='Номер абонемента')
    date_open_sub = models.DateTimeField(auto_now_add=True, verbose_name='Дата открытия')
    id_library = models.ForeignKey(
        'Library',
        on_delete=models.CASCADE,
        related_name='Library_reader',
        verbose_name='ID библиотеки',
        null=True,
        blank=True
    )
    id_reader = models.ForeignKey(
        'Reader',
        on_delete=models.CASCADE,
        related_name='reader_subscription',
        verbose_name='ID читателя',
        null=True,
        blank=True
    )
    is_deleted = models.BooleanField(default=False, verbose_name='Удалить')

    def __str__(self):
        return self.number_subscription

    class Meta:
        unique_together = ['id_reader', 'id_library']
        verbose_name = 'абонемент'
        verbose_name_plural = 'Абонемент'