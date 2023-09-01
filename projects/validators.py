from django.core.exceptions import ValidationError


def validate_profile(prop):
    if not prop:
        raise ValidationError("Property cannot be empty.")

    if len(prop) >= 500:
        raise ValidationError("Property is too long (max 500 characters).")


def validate_project(prop):
    if not prop:
        raise ValidationError("Property cannot be empty.")

    if len(prop) >= 500:
        raise ValidationError("Property is too long (max 500 characters).")


def validate_certifying_institution(prop):
    if not prop:
        raise ValidationError("Property cannot be empty.")

    if len(prop) >= 500:
        raise ValidationError("Property is too long (max 500 characters).")


def validate_certificate(prop):
    if not prop:
        raise ValidationError("Property cannot be empty.")

    if len(prop) >= 500:
        raise ValidationError("Property is too long (max 500 characters).")
