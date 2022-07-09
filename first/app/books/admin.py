from django.contrib import admin
from .models import Book, PublishingHouse, Author, BooksInAuthor

'''list_display - какие атрибуты будут выводится на экран
list_display_links - какие атрибуты будут ссылками
search_fields - по каким полям будет происходить поиск
list_editable - какие поля можно изменить в таблице
list_filter - по каким полям будет происходить фильтр
fieldsets - '''


class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'book_name', 'description', 'id_publishing_house',
                    'date_creation', 'date_add', 'book_img', 'is_deleted')
    list_display_links = ('id', 'book_name')

    search_fields = ('id', 'book_name', 'id_publishing_house', 'date_creation', 'date_add', 'is_deleted')
    list_editable = ('is_deleted', 'book_img',)
    list_filter = ('date_creation', 'date_add', 'is_deleted')


class PublishingHouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'publishing_house_name', 'address', 'contact_phone', 'email',
                    'website_link', 'date_add', 'is_deleted')
    list_display_links = ('id', 'publishing_house_name')
    search_fields = ('id', 'publishing_house_name', 'address', 'contact_phone', 'email', 'website_link', 'date_add',
                     'is_deleted')
    list_editable = ('is_deleted',)
    list_filter = ('date_add', 'is_deleted')
    fieldsets = (
        (
            (None, {
                'fields': ('publishing_house_name', 'address',)
            }),
            ('Контакты', {
                'fields': ('contact_phone', 'email', 'website_link',)
            }),
        )
    )


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'father_name', 'country',
                    'birthday', 'languages', 'date_add', 'is_deleted')
    list_display_links = ('id', 'first_name', 'last_name', 'date_add')
    search_fields = ('id', 'first_name', 'last_name', 'country', 'birthday', 'languages', 'date_add', 'is_deleted')
    list_editable = ('is_deleted',)
    list_filter = ('first_name', 'last_name', 'country', 'date_add', 'is_deleted')

    inlines = [
        BooksInAuthor,
    ]


admin.site.register(Book, BooksAdmin)
admin.site.register(PublishingHouse, PublishingHouseAdmin)
admin.site.register(Author, AuthorAdmin)