import  random
import string
import time
import uuid
from django.db import  models
from  django.conf import settings
from django.contrib.auth.models import  AbstractUser,Group
from django.db.models.signals import  post_save
from  django.dispatch import receiver
from django.utils import timezone
from rest_framework.authtoken.models import  Token
from users.manager import  UserManager
from employees.models import  Position


# custom user/manager registration model
class User(AbstractUser):

    name = models.CharField(max_length=200, editable=True, blank=False, null=True)
    national_id = models.CharField(max_length=20, unique=True,null=True)  # national_id should be unique
    phone_number = models.CharField(max_length=15, unique=True,null=True,default='+2507445566667')  # phone number should be unique
    email = models.EmailField(max_length=200, unique=True, null=True, blank=False)  # email. should be unique

    statues = {
        ('ACTIVE', 'ACTIVE'),
        ('INACTIVE', 'INACTIVE'),
    }

    status = models.CharField(max_length=50, choices=statues, default='ACTIVE')
    registered_time = models.DateTimeField(auto_now_add=True, editable=False)
    position=models.ForeignKey(Position,on_delete=models.CASCADE,null=True)
    date_of_birth = models.DateField(null=True)
    USERNAME_FIELD = 'national_id'



    objects = UserManager()



    def save(self, *args, **kwargs):
        if self.national_id:
            self.name = self.national_id

        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.national_id



