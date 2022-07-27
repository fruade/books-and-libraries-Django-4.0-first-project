import re
from django.core.exceptions import ValidationError


def validation_book_name(value: str):
    if re.fullmatch(r'[A-ZА-ЯЁ0-9].*', value):
    #if value.split()[0].istitle() or value[0].isdigit():
        return value
    raise ValidationError(message='Таких книг не существует, попробуй еще!')
