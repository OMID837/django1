from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')
    avatar = models.ImageField(verbose_name='', upload_to='users')
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'