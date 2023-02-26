from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_student= models.BooleanField('Is student', default=False)
    is_teacher = models.BooleanField('Is teacher', default=False)
    is_principal = models.BooleanField('Is principal', default=False)
    is_institutionadmin = models.BooleanField('Is institutionadmin', default=False)
    is_organisationadmin = models.BooleanField('Is organisationadmin', default=False)
    orgname = models.CharField(max_length=100)
    instname=models.CharField(max_length=100)
    principal = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)
    student = models.CharField(max_length=100)
