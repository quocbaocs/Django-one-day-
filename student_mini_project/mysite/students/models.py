from django.db import models

# Create your models here.
class Student(models.Model):
    studentNo = models.CharField(db_column='student_no', max_length=20, unique=True)

    studentName = models.CharField(db_column='student_name', max_length=50)

    address = models.CharField(db_column='address', max_length=100)