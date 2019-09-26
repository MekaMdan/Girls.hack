from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 50, validators=[MinLengthValidator(3)])
    last_name = models.CharField(max_length = 250, validators=[MinLengthValidator(3)])
    email = models.EmailField()
    matricula = models.CharField(max_length = 9, validators=[MinLengthValidator(9)])