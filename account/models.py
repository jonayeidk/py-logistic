from django.db import models

from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.

PERMISSION_CHOICES = (
    (1, 'Admin'),
    (2, 'Assistant Admin'),
    (3, 'Data Entry Operator'),
    (4, 'Management Officer'),
    (5, 'Employement'),
)


class UserManger(BaseUserManager):

    def create_user(
            self, 
            email, 
            username,
            first_name=None,
            last_name=None,
            phone=None,
            role=5, 
            date_of_birth=None, 
            password=None
        ):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            role=role,
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser):
    first_name = models.CharField(max_length=100,blank=True)
    last_name = models.CharField(max_length=100,blank=True)
    username = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    phone = models.IntegerField(blank=True)
    role = models.IntegerField(
        choices=PERMISSION_CHOICES,default=5)
    date_of_birth = models.DateField(blank=True, null=True)



