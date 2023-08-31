from django.db import models

from projects.validators import validate_profile


class Profile(models.Model):
    name = models.CharField(max_length=100, validators=[validate_profile])
    github = models.URLField(validators=[validate_profile])
    linkedin = models.URLField(validators=[validate_profile])
    bio = models.TextField(validators=[validate_profile])

    def __str__(self):
        return self.name
