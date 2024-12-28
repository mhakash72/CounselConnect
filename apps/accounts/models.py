from django.contrib.auth.models import AbstractUser,Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    """
    Custom user model for CounselConnect.
    Extends Django's AbstractUser to add role-based authentication.
    """
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Change this to a unique name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Change this to a unique name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    class Roles(models.TextChoices):
        ADMIN = 'ADMIN', _('Admin')
        CHAMBERS_ADMIN = 'CHAMBERS_ADMIN', _('Chambers Admin')
        BARRISTER = 'BARRISTER', _('Barrister')
        CLERK = 'CLERK', _('Clerk')
        SOLICITOR = 'SOLICITOR', _('Solicitor')
        PUBLIC = 'PUBLIC', _('Public')

    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.PUBLIC
    )
    phone_number = models.CharField(max_length=20, blank=True)
    is_verified = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

class Profile(models.Model):
    """
    Extended profile information for users.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    secondary_email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"