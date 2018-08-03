from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(auto_now_add=True)
    age = models.IntegerField()
    email = models.EmailField()
    contact = models.IntegerField()


class Category(models.Model):
    name = models.CharField(max_length=50)


class Student_category(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)


class Instructor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(auto_now_add=True)
    title = models.CharField()
    email = models.EmailField()
    contact = models.IntegerField()


class Class_Type(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)


class Class(models.Model):
    class_type_id = models.ForeignKey(Class_Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    start = models.DateField(auto_now_add=True)
    end = models.DateField(auto_now=True)
    completed = models.BooleanField(default=True)


class Class_schedule(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()





