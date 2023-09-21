from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from urllib import request
from django.core.files import File
import os
import base64
import uuid
from .managers import UserManager
# from tempfile import NamedTemporaryFile
from django.core.files.base import ContentFile
# Create your models here.
ADMIN = 1
USER = 2

ROLE_CHOICES = (
    (ADMIN, 'Admin'),
    (USER, 'User'),
)






class User(AbstractUser):
    name = models.CharField(max_length=255,null=True,blank=True)
    username = None
    user_photo = models.FileField(null=False,blank=False,default='default_user.jpeg')
    gender= models.CharField(max_length=255,null=True,blank=True)
    phone= models.BigIntegerField(null=True,blank=True)
    email= models.EmailField(unique=True,null=True,blank=True)
    dob= models.DateField(null=True,blank=True)
    otp = models.CharField(max_length=50,null=True,blank=True)
    status= models.BooleanField(null=True,blank=True,default=1)
    role_id =models.IntegerField(null=True,blank=True,choices=ROLE_CHOICES,default = 2)
    profession= models.CharField(max_length=255,null=True,blank=True)
    pincode = models.IntegerField(null=True,blank=True)
    created_by= models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated = models.DateField(null=True,blank=True)
    updated_by = models.CharField(max_length=255,null=True,blank=True)
    is_active = models.BooleanField(default=False,)
    photo_url = models.TextField(null=True,blank=True)
    user_notification_token = models.CharField(max_length=255,null=True,blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
    
    # def __str__(self):
    #     return self.email  



    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    # def save(self, *args, **kwargs):
    #     if self.photo_url and  self.user_photo == 'default_user.png':
    #         if not self.photo_url:
    #             pass
    #         img_tmp =  NamedTemporaryFile(delete=True)
    #         result = request.urlretrieve(self.photo_url)
    #         self.user_photo.save(
    #                 os.path.basename(self.photo_url+".jpg"),
    #                 File(open(result[0], 'rb')))
    #     super(User, self).save(*args, **kwargs)
    
    # def save(self, *args, **kwargs):
    #     if self.photo_url and  self.user_photo == 'default_user.png':
    #         name = f'{uuid.uuid4()}'+".jpg"
    #         data = base64.b64decode(self.photo_url)
    #         self.user_photo = ContentFile(data,name)
    #     super(User, self).save(*args, **kwargs)
    
    
    
    
    # def has_perm(self, perm, obj=None):




    #     return True


    # class Meta:
    #     db_table = "
