from datetime import date

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import MinLengthValidator, MaxLengthValidator

from .managers import ProfileManager


def directory_path_users(instance, filename):
    if instance.position == 2:
        x = 'users'
    elif instance.position == 1:
        x = 'staff'
    else:
        x = 'admins'

    return ('users/{}/{}/{}/{}').format(
        x,
        date.today(),
        instance.email,
        filename)


POSITION_LIST = [
    (0, 'Admin'),
    (1, 'Head'),
    (2, 'Manager'),
    (3, 'User')
]


class Profile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True)
    phone = models.CharField(
        max_length=12,
        unique=False,
        validators=[
            MinLengthValidator(12, _('Минимальная длина 12 символов')),
            MaxLengthValidator(12, _('Максимальная длина 12 символов')),
        ])
    name = models.CharField(
        max_length=60,
        unique=False)
    position = models.IntegerField(
        blank=True,
        null=True,
        choices=POSITION_LIST,
        default=3)
    photo = models.ImageField(
        blank=True,
        null=True,
        default='default.jpg',
        upload_to=directory_path_users)
    bio = models.TextField(
        default='',
        unique=False)

    is_admin = models.BooleanField(
        default=False)
    is_staff = models.BooleanField(
        default=False)
    is_active = models.BooleanField(
        default=True)
    is_blocked = models.BooleanField(
        default=False)
    is_deleted = models.BooleanField(
        default=False)
    is_confirm = models.BooleanField(
        default=False)


    datedel = models.DateField(
        blank=True,
        null=True)
    created = models.DateTimeField(
        auto_now_add=True,
        null=True)
    updated = models.DateTimeField(
        auto_now=True,
        null=True)

    groups = models.ManyToManyField(
        Group,
        blank=True)

    objects = ProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save()

    class Meta:
        db_table = 'Users'


class AmoCRMContacts(models.Model):
    contact_id = models.IntegerField(
        blank=True,
        null=True,
        default='')

    email = models.EmailField(
        unique=False)

    phone = models.CharField(
        max_length=15,
        unique=False)

    name = models.CharField(
        max_length=60,
        unique=False)

    country = models.CharField(
        max_length=30,
        default='')

    def __str__(self):
        return self.contact_id

    def save(self, *args, **kwargs):
        super().save()

    class Meta:
        db_table = 'CRM Contacts'


class AmoCRMDeals(models.Model):
    contact_id = models.IntegerField(
        default=0)

    email = models.EmailField(
        unique=False)

    phone = models.CharField(
        max_length=30,
        default='')

    created_at = models.CharField(
        max_length=30,
        default='')

    update_at = models.CharField(
        max_length=30,
        default='')

    price = models.IntegerField(
        default=0)

    quantity = models.IntegerField(
        default=1)

    status = models.CharField(
        max_length=40,
        default='')

    deal_id = models.CharField(
        max_length=20,
        default=0)

    payment_type = models.CharField(
        max_length=40,
        default='')

    offer_id = models.CharField(
        max_length=20,
        default=0)

    reason = models.CharField(
        max_length=30,
        default=0)

    def __str__(self):
        return self.deal_id

    def save(self, *args, **kwargs):
        super().save()

    class Meta:
        db_table = 'CRM Deals'
