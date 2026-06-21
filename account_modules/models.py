from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(upload_to='media',verbose_name='تصویر اواتار',null=True,blank=True)
    email_active_code=models.CharField(max_length=50,verbose_name='کد فعال سازی')
    phone_number=models.CharField(max_length=11,verbose_name='شماره تماس')
    verification_code = models.CharField(max_length=100,blank=True,null=True,verbose_name='فعال سازی فراموشی رمز')
    about_user = models.TextField(null=True, blank=True, verbose_name='درباره من')
    address = models.TextField(null=True, blank=True, verbose_name='آدرس')

    class Meta:
        verbose_name='کاربر'
        verbose_name_plural='کاربران'

    def __str__(self):
        if self.first_name and self.last_name:
            return self.get_full_name()
        return self.email
