from rest_framework import serializers
from .models import Student, Department, Course, Professor, Subject, Avaliation, Class

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department 
        fields = '__all__'

class CourseSerializer (serializers.ModelSerializer):
    class Meta:
        model = Course 
        fields = '__all__'       

class ProfessorSerializer (serializers.ModelSerializer):
    class Meta:
        model = Professor 
        fields = '__all__'       

class SubjectSerializer (serializers.ModelSerializer):
    class Meta:
        model = Subject 
        fields = '__all__'  

class AvaliationSerializer (serializers.ModelSerializer):
    class Meta:
        model = Avaliation 
        fields = '__all__'  

class ClassSerializer (serializers.ModelSerializer):
    class Meta:
        model = Class 
        fields = '__all__'  