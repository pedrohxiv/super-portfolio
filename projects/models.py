from django.db import models

from projects.validators import (
    validate_profile,
    validate_project,
    validate_certifying_institution,
    validate_certificate,
)


class Profile(models.Model):
    name = models.CharField(max_length=100, validators=[validate_profile])
    github = models.URLField(validators=[validate_profile])
    linkedin = models.URLField(validators=[validate_profile])
    bio = models.TextField(validators=[validate_profile])

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50, validators=[validate_project])
    description = models.TextField(
        max_length=500,
        validators=[validate_project],
    )
    github_url = models.URLField(validators=[validate_project])
    keyword = models.CharField(max_length=50, validators=[validate_project])
    key_skill = models.CharField(max_length=50, validators=[validate_project])
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="projects",
        default=2,
    )

    def __str__(self):
        return self.name


class CertifyingInstitution(models.Model):
    name = models.CharField(
        max_length=50,
        validators=[validate_certifying_institution],
    )
    url = models.URLField(validators=[validate_certifying_institution])

    def __str__(self):
        return self.name


class Certificate(models.Model):
    name = models.CharField(max_length=100, validators=[validate_certificate])
    certifying_institution = models.ForeignKey(
        CertifyingInstitution,
        on_delete=models.CASCADE,
        related_name="certificates",
        default=2,
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        validators=[validate_certificate],
    )
    profiles = models.ManyToManyField(
        Profile,
        related_name="certificates",
        default=2,
    )
