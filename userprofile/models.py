from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import PermissionsMixin

# Create your models here.

class UserProfileManager(BaseUserManager):
    # use_in_migrations = True
    def _create_user(self, email, password, profile_id, mobile, country, name, is_staff, is_active, is_superuser):
        if not email:
            raise ValueError('Email required')
        email = self.normalize_email(email)
        user = self.model(email=email, profile_id=profile_id, mobile=mobile, country=country, name=name, is_staff=is_staff, is_active=is_active, is_superuser= is_superuser)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, profile_id, mobile, country, name, password=None, is_staff=True, is_active=True, is_superuser=False):
        # extra_fields.setdefault('is_staff', False)
        # extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, profile_id=profile_id, mobile=mobile, country=country, name=name, is_staff=is_staff, is_active=is_active, is_superuser= is_superuser)
    
    def create_superuser(self, email, password, profile_id, mobile, country, name,is_staff=True, is_active=True, is_superuser=True):
        # extra_fields.setdefault('is_staff', True)
        # extra_fields.setdefault('is_superuser', True)
        # extra_fields.setdefault('is_active', True)
        if is_staff is not True:
            raise ValueError(
                'Superuser must be a staff'
            )
        if is_superuser is not True:
            raise ValueError(
                'Superuser must be a superuser'
            )
        return self._create_user(email, password, profile_id=profile_id, mobile=mobile, country=country, name=name, is_staff=is_staff, is_active=is_active, is_superuser= is_superuser)
    
class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True,max_length=255,blank=False)
    profile_id = models.CharField('profile id',max_length=150,blank=True)
    name = models.CharField('name',max_length=150,blank=True)
    country = models.CharField('country',max_length=150,blank=True)
    mobile= models.PositiveBigIntegerField('mobile',null=True,blank=True)
    is_staff = models.BooleanField('staff status',default=False)
    is_active = models.BooleanField('active',default=False)
    is_superuser = models.BooleanField('superuser',default=False)
  
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['profile_id', 'name', 'country', 'mobile']

    objects = UserProfileManager()

    def __str__(self):
        return self.email
    
    def full_name(self):
        return self.first_name+" "+self.last_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True