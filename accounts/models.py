from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        email_user = self.model(email=email, **extra_fields)
        email_user.set_password(password)
        email_user.save(using=self._db)
        return email_user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active=True.')
        email = self.normalize_email(email)
        email_user = self.model(email=email, password=password)
        email_user.set_password(password)
        email_user.save(using=self._db)
        return email_user

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if email is None:
            raise ValueError('Email address is required')
        email = self.normalize_email(email).lower()
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class UserModel(AbstractUser):
    username = None
    email = models.EmailField(max_length=255, unique=True)

    # Added related_name to fix clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Add unique related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Add unique related_name
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    objects = CustomUserManager()  # Assign CustomUserManager to the model

    def get_full_name(self):
        return f"{self.first_name} | {self.last_name}"

    def __str__(self):
        return self.email

    def __repr__(self):
        return self.email


str(object)
