import re
from django.core.exceptions import ValidationError


def validation_address(value: str):
    pattern = r'Россия,\sгор.\s[А-ЯЁ][а-яё].*,\sул.\s[А-ЯЁ][а-яё].*,\sдом\s[0-9]+'
    if re.fullmatch(pattern=pattern, string=value):
        return value
    raise ValidationError(message='Что то пошло не так, попробуй в формате [Россия, гор. ..., ул. ..., дом ...]!')