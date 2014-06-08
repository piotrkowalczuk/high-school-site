from django.db import models
from user.managers import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):

    ROLE_CHOICES = (
        ('member', 'Member'),
        ('personnel', 'Personnel'),
    )

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    username = models.EmailField(unique=True, db_index=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    activation_code = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    photo = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    birth_date = models.DateTimeField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __unicode__(self):
        return self.get_fullname()

    def get_fullname(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']
