from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.
# this is actually responsible to create and save the data into the database
class AccountCreationManager(BaseUserManager):
     
     # create account that are not staff
     
    def create_user(self, first_name, last_name, username, email, password=None):
        """
        Creates and saves a User with the given infos and password.
        """
        if not email:
            raise ValueError("Users must have an email address")
        
        if not username:
            raise ValueError("User must have an username")
        

        user = self.model(
            first_name = first_name,
            last_name = last_name,
            email=self.normalize_email(email),
            username = username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    # create account those are staff

    def create_superuser(self, first_name, last_name, username, email, password=None):
        """
        Creates and saves a superuser with the given infos and password.
        """
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True

        user.save(using=self._db)
        return user




# this is the model to creating  an account

class Account(AbstractBaseUser):

    # basic info
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=15)

    # auto generate info
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)

    # user access level
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    # selecting custom manager
    objects = AccountCreationManager()


    # login field 
    USERNAME_FIELD = 'email'

    # other require field except password field
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email
    

    def has_perm(self, perm, obj=None):
            "Does the user have a specific permission?"
            # Simplest possible answer: Yes, always
            return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
