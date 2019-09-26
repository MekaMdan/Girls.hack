from django.db import models
from django.core.validators import MinLengthValidator, int_list_validator,MinValueValidator, MaxValueValidator, MaxLengthValidator
from django.db.models import DecimalField
from django.contrib.auth.models import AbstractUser



# Create your models here.


class Department(models.Model):

    
    department_name = models.CharField(max_length=70, validators=[MinLengthValidator(3)])

    def __str__(self):
        return self.department_name

    class Meta:
        db_table = 'department'
        ordering = ['department_name']


class Course(models.Model):

    course_name = models.CharField(max_length=70, validators=[MinLengthValidator(3)])
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'course'
        ordering = ['course_name']

    def __str__(self):
        return self.course_name


class Student(AbstractUser):  

    nome = models.CharField(max_length=50, validators=[MinLengthValidator(3)])
    sobrenome = models.CharField(max_length=200, validators=[MinLengthValidator(4)], default = '')
    email = models.EmailField()
    password = models.CharField(max_length = 300, validators=[MinLengthValidator(6)], default = '')
    course = models.ForeignKey(Course, on_delete=models.PROTECT, default = '')

    def __str__(self):
        return self.nome
    class Meta:
        db_table = 'student' 
                   
class Professor(models.Model):

    class Meta:
        db_table = 'professor'
        ordering = ['nota']
    
    name = models.CharField(max_length=50, validators=[MinLengthValidator(3)])
    last_name = models.CharField(max_length=200, validators=[MinLengthValidator(3)])
    nota = DecimalField(max_digits = 4,decimal_places=2,default=5, validators = [MinValueValidator(0), MaxValueValidator(5)])
    dept = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name

class Subject(models.Model):
    
    subject_nome = models.CharField(max_length=70, validators=[MinLengthValidator(3)])
    subject_department = models.ForeignKey(Department,on_delete=models.CASCADE)
    subject_nmo = models.CharField(max_length=6, validators=[MinLengthValidator(6), int_list_validator(allow_negative=False)])
        
    class Meta:
        db_table = 'subject'
        ordering = ['subject_department', 'subject_nome']

    def __str__(self):
        return self.subject_nome

class Avaliation(models.Model):
    avaliation_student = models.ForeignKey(Student, on_delete=models.CASCADE)
    avaliation_professor = models.ForeignKey(Professor, on_delete=models.PROTECT)
    avaliation_grade = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(5)])
    avaliation_text = models.TextField()
    avaliation_date = models.DateField(auto_now_add = True)
    avaliation_subject = models.ForeignKey(Subject, on_delete=models.PROTECT)

    class Meta:
        db_table = 'avaliation'
        ordering = ['avaliation_date']

    def __str__(self):
        return self.avaliation_text

class Classes(models.Model):
    class_subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    class_avaliation = models.ForeignKey(Avaliation, on_delete=models.CASCADE)
    class_grades = DecimalField(max_digits = 4,decimal_places=2,default=5, validators = [MinValueValidator(0), MaxValueValidator(5)])
    class Meta:
        db_table = 'class_id'
        ordering = ['class_avaliation']

    def __str__(self):
        return self.subject_nome