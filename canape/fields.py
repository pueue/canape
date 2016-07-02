from django.forms import Field
from django.core.validators import validate_email


class MultiEmailField(Field):
    def to_python(self, value):
        if not value:
            return []
        value = [email.strip() for email in value.strip().split(',')]
        return list(set(value))

    def validate(self, value):
        super(MultiEmailField, self).validate(value)
        for email in value:
            validate_email(email)
