from django.db import models

from django.contrib.auth.models import (
                        AbstractUser,
                        BaseUserManager
                    )

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Vous devez fournir un email valide")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(
                "Superuser must have is_staff=True"
            )

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None

    email =  models.EmailField('Adresse Email', unique=True)

    first_name = models.CharField(
        'Prénom',
         max_length=255)

    last_name = models.CharField(
        'Nom',
         max_length=255)

    slug = models.SlugField(blank=True)

    is_doctor = models.BooleanField(default=False)
    is_active = models.BooleanField('Actif', default=True)
    last_ip_adress = models.CharField(
        'Adresse IP',
        max_length=39,
        blank=True,
        null=True
    )
    last_visit = models.DateTimeField(
        'Date de dernière visite',
        blank=True,
        null=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
