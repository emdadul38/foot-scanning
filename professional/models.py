from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)

# Create your models here.
class Address(models.Model):
    street_1    = models.CharField(max_length=255, null=True)
    street_2    = models.CharField(max_length=255, null=True, blank=True)
    city        = models.CharField(max_length=100, null=True)
    zipcode     = models.CharField(max_length=50)
    country     = models.CharField(max_length=100)
    
    def __str__(self):
        return 'Street_1: %s, Street_2: %s, City: %s, Country: %s, %s ' %(self.street_1, self.street_2, self.city, self.city, self.country)
    
    REQUIRED_FIELDS = [ 'street_1', 'city', 'zipcode', 'country',] 

class Organization(models.Model):
    name    = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name
    
class UserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, gender, birth_date, phone,  password=None):
        if not email:
            raise ValueError("Users must be an email address")
        
        if not username:
            raise ValueError("Users must be an username")
        
        if not first_name:
            raise ValueError("Users must be an first_name")
        
        if not last_name:
            raise ValueError("Users must be an last_name")
        
        if not gender:
            raise ValueError("Users must be an gender")
        
        if not birth_date:
            raise ValueError("Users must be Birth date")
        
        if not phone:
            raise ValueError("Users must be Phone")
                        
        user_obj = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            gender = gender,
            birth_date = birth_date,
            phone = phone,
        )
        user_obj.set_password(password)     #change user password   
        
        user_obj.save(using=self._db)
        return user_obj

    
    def create_superuser(self, email, username, first_name, last_name, gender, birth_date, phone, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            username = username,
            first_name = first_name,
            last_name = last_name,
            gender = gender,
            birth_date = birth_date,
            phone = phone
        )
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user 
    
class User(AbstractBaseUser):
    GENDER_OPTION = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
    username                = models.CharField(max_length=30, unique=True, null=True, blank= True)
    first_name 				= models.CharField(max_length=255, unique=False)
    middle_name 			= models.CharField(max_length=255, unique=False, blank=True)
    last_name 				= models.CharField(max_length=255, unique=False)
    gender 				    = models.CharField(max_length=6, choices=GENDER_OPTION, default='male')
    birth_date 				= models.DateField(verbose_name=None, auto_now=False)
    phone                   = models.CharField(max_length=50, null=True)
    organization            = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True)
    shipping_address        = models.OneToOneField(Address, related_name='address_as_shipping', on_delete=models.CASCADE, null=True)
    billing_address         = models.OneToOneField(Address, related_name='address_as_billing', on_delete=models.CASCADE, null=True)
        
    date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin				= models.BooleanField(default=False)
    is_active				= models.BooleanField(default=True)
    is_staff				= models.BooleanField(default=False)
    is_superuser			= models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'    #username
    
    objects = UserManager()
    
    # email and password are required by default
    REQUIRED_FIELDS = [ 'username', 'first_name', 'last_name', 'gender', 'birth_date', 'phone',]    # '['first_name']
    
    def __str__(self):
        return self.email
       
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

class Professional(models.Model):
    USER_TYPE = (
        ('Practitioner', 'Practitioner'),
        ('Staff', 'Staff'),
    )
    
    SIZE_UNIT = (
        ('meter', 'Meter'),
        ('foot', 'Foot'),
    )
    
    WEIGHT_UNIT = (
        ('kg', 'kg'),
        ('lb', 'lb'),
    )
    
    user        = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    unit_size   = models.CharField(max_length=10, choices=SIZE_UNIT, default='meter')
    weight_unit = models.CharField(max_length=2, choices=WEIGHT_UNIT, default='kg')
    user_type   = models.CharField(max_length=15, choices=USER_TYPE, default='Practitioner',)   
        
    def __str__(self):
        return f"{self.user.first_name} {self.user.middle_name} {self.user.last_name}" 

class Patient(models.Model):
    user        = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    practitioner= models.ForeignKey(Professional, on_delete=models.SET_NULL, null=True)
    height       = models.PositiveIntegerField()
    weight       = models.PositiveIntegerField()
    
    REQUIRED_FIELDS = [ 'user', 'practitioner', 'height', 'weight',]  
    
    def __str__(self):
        return self.user.email

class Album(models.Model):
    name    = models.CharField(max_length=255)
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True, related_name='patient')
    created_by = models.ForeignKey(Professional, on_delete=models.SET_NULL, null=True, blank=True, related_name='professional')
    date_created = models.DateTimeField(verbose_name='date created', auto_now_add=False)
    
    def __str__(self):
        return self.name
    
class Scan(models.Model):
    SCAN_TYPE = (
        ('foot', 'Foot'),
        ('ulcer', 'Ulcer')
    )
    
    name    = models.CharField(max_length=255)
    album   = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='album')
    scan_type = models.CharField(max_length=10, choices=SCAN_TYPE, default='foot')
    
    def __str__(self):
        return self.name