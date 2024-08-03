from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, username, name, password=None):

        if not email:
            raise ValueError('Users must provide an email address')
        if not username:
            raise ValueError('Users must provide a username')
        if not name:
            raise ValueError('Users must provide a name')
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, name, password=None):
        user = self.create_user(
            email=email,
            username=username,
            name=name,
            password=password
        )
        user.is_admin= True
        user.save(using=self._db)
        return user
class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address',max_length=75,
                              unique=True)
    username = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=55)
    password = models.CharField(max_length=50)
    objects = UserManager()
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['username','name']

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
class UrlObject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    url = models.CharField(max_length=100)

    def __str__(self) :
        return self.urlobject


