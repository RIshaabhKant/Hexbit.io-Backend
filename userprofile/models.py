from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

# Create your models here.


class UserProfileManager(BaseUserManager):
    # use_in_migrations = True
    def _create_user(self, email, password, mobile, country, name, pan_number, legal_entity_name, incorporation_type, fssai_number, gst_number, bank_account, account_number, ifsc_code, is_staff, is_active, is_superuser):
        if not email:
            raise ValueError('Email required')
        email = self.normalize_email(email)
        user = self.model(email=email, mobile=mobile, country=country, name=name, pan_number=pan_number, legal_entity_name=legal_entity_name, incorporation_type=incorporation_type, fssai_number=fssai_number,
                          gst_number=gst_number, bank_account=bank_account, ifsc_code=ifsc_code, account_number=account_number, is_staff=is_staff, is_active=is_active, is_superuser=is_superuser)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, mobile, country, name, pan_number, legal_entity_name, incorporation_type, fssai_number, gst_number, bank_account, ifsc_code, account_number, password=None, is_staff=True, is_active=True, is_superuser=False):

        return self._create_user(email, password, pan_number=pan_number, legal_entity_name=legal_entity_name, incorporation_type=incorporation_type, fssai_number=fssai_number, gst_number=gst_number, bank_account=bank_account, ifsc_code=ifsc_code, account_number=account_number, mobile=mobile, country=country, name=name, is_staff=is_staff, is_active=is_active, is_superuser=is_superuser)

    def create_superuser(self, email, password, pan_number, legal_entity_name, incorporation_type, fssai_number, gst_number, bank_account, ifsc_code, account_number, mobile, country, name, is_staff=True, is_active=True, is_superuser=True):
        if is_staff is not True:
            raise ValueError(
                'Superuser must be a staff'
            )
        if is_superuser is not True:
            raise ValueError(
                'Superuser must be a superuser'
            )
        return self._create_user(email, password, pan_number=pan_number, legal_entity_name=legal_entity_name, incorporation_type=incorporation_type, fssai_number=fssai_number, gst_number=gst_number, bank_account=bank_account, ifsc_code=ifsc_code, account_number=account_number, mobile=mobile, country=country, name=name, is_staff=is_staff, is_active=is_active, is_superuser=is_superuser)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=255, blank=False)
    name = models.CharField('name', max_length=150, blank=True)
    country = models.CharField('country', max_length=150, blank=True)
    mobile = models.PositiveBigIntegerField('mobile', null=True, blank=True)
    pan_number = models.CharField(
        'pan_number', max_length=10, unique=True, blank=True)
    legal_entity_name = models.CharField(
        'legal_entity_name', max_length=100, blank=True)
    incorporation_type = models.CharField(
        'incorporation_type', max_length=100, blank=True)
    fssai_number = models.CharField('fssai_number', max_length=14, blank=True)
    gst_number = models.CharField('gst_number', max_length=15, blank=True)
    bank_account = models.CharField('bank_account', max_length=100, blank=True)
    account_number = models.CharField(
        'account_number', max_length=17, blank=True)
    ifsc_code = models.CharField('ifsc_code', max_length=11, blank=True)

    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=False)
    is_superuser = models.BooleanField('superuser', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'country', 'mobile', 'pan_number', 'legal_entity_name',
                       'incorporation_type', 'fssai_number', 'gst_number', 'bank_account', 'account_number', 'ifsc_code']

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
