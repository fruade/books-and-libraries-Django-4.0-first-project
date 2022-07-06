from django.contrib import admin
from .models import Library, Subscription, Reader


class LibraryAdmin(admin.ModelAdmin):
    list_display = ('id', 'library_name', 'address', 'contact_phone',
                    'website_link', 'date_add', 'is_deleted')
    list_display_links = ('id', 'library_name', 'website_link')

    search_fields = ('id', 'library_name', 'date_add', 'is_deleted')
    list_editable = ('is_deleted', 'address')
    list_filter = ('library_name', 'date_add', 'is_deleted')


class ReaderAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'father_name', 'birthday',
                    'contact_phone', 'email', 'date_add', 'is_deleted')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('id', 'first_name', 'last_name', 'birthday', 'date_add', 'is_deleted')
    list_editable = ('is_deleted',)
    list_filter = ('first_name', 'last_name', 'date_add', 'is_deleted')

    fieldsets = (
        (
            (None, {
                'fields': ('first_name', 'last_name', 'father_name', 'birthday',)
            }),
            ('Контакты', {
                'fields': ('contact_phone', 'email')
            }),
        )
    )


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'number_subscription', 'date_open_sub', 'id_library', 'id_reader', 'is_deleted')
    list_display_links = ('number_subscription', 'id_library', 'id_reader')
    search_fields = ('id', 'number_subscription', 'date_open_sub', 'id_library', 'id_reader')
    list_editable = ('is_deleted',)
    list_filter = ('number_subscription', 'date_open_sub')


admin.site.register(Library, LibraryAdmin)
admin.site.register(Reader, ReaderAdmin)
admin.site.register(Subscription, SubscriptionAdmin)