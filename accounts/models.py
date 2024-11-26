from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self,first_name,last_name,email,username,password=None):
        if not username:
            raise ValueError("Username can not be blank")

        if not email:
            raise ValueError("EMail can not be blanked")
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self,first_name,last_name,email,username,password=None):
        user = self.create_user(
            first_name,
            last_name,
            email,
            username,
            password

        )
        
        user.is_admin =True 
        user.is_active = True 
        user.is_staff = True 
        user.is_super = True
        user.save(using=self._db)
        return user
 


class User(AbstractBaseUser):

    RESTURANT = 1
    CUSTOMER =2
    
    ROLE_CHOICE = (
        (RESTURANT,'Resturant'), (CUSTOMER,'Customer')
    )
    
    first_name  = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    username= models.CharField(max_length=20)
    phone_number = models.CharField(max_length=12)
    role= models.PositiveSmallIntegerField(choices=ROLE_CHOICE,blank=True,null=True)

    date_joined= models.DateTimeField(auto_now_add=True)
    last_login  = models.DateTimeField(auto_now_add=True)
    created_date  = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff  =models.BooleanField(default=False)
    is_super = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name","last_name","username"]

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        
        return self.is_admin
    
    def has_module_perms(self, app_label):
        
        return True
