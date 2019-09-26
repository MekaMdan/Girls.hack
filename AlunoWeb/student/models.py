from django.db import models

# Create your models here.

class Student(models.Model):
    class Meta:
        db_table = 'student'
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    matricula = models.CharField(max_length=200)
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.nome
