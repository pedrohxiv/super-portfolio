from django.core.exceptions import ValidationError


def validate_profile(prop):
    if not prop:
        raise ValidationError("Property cannot be empty.")

    if len(prop) >= 500:
        raise ValidationError("Property is too long (max 500 characters).")
