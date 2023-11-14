# Models da aplicação 

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager,
    PermissionsMixin
)
from django.utils import timezone

class UserManager( BaseUserManager ):
    """Manager for users."""

    def create_user(self, email, password = None, **extra_fiels):
        """Create, save and return a new user,"""
        if not email:
            raise ValueError("Voce precisa de um email")
        
        user = self.model(email=self.normalize_email(email), **extra_fiels)
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email, password):
        """Create, save and return a new super user,"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
    

class User(AbstractBaseUser, PermissionsMixin):
    """User in system"""
    # email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, null=False)
    first_name = models.CharField(max_length=255, null=False)
    # cpf = models.CharField(null = True, upload_to=user_image_field)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=)