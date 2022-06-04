from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.user.username + " | " + self.user.email