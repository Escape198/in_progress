from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import MinLengthValidator, MaxLengthValidator

from datetime import date


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
        'Почта',
        unique=True)
    phone = models.CharField(
        'Телефон',
        max_length=12,
        unique=False,
        validators=[
            MinLengthValidator(12, _('Минимальная длина 12 символов')),
            MaxLengthValidator(12, _('Максимальная длина 12 символов')),
        ])
    name = models.CharField(
        'Логин',
        max_length=60,
        unique=False)
    position = models.IntegerField(
        'Роль',
        blank=True,
        null=True,
        choices=POSITION_LIST,
        default=3)
    photo = models.ImageField(
        'Фото',
        blank=True,
        null=True,
        default='default.jpg',
        upload_to=directory_path_users)
    bio = models.TextField(
        'Описание профиля',
        default='',
        unique=False)

    is_admin = models.BooleanField(
        'Администратор?',
        default=False)
    is_staff = models.BooleanField(
        'Сотрудник?',
        default=False)
    is_active = models.BooleanField(
        'Активен?',
        default=True)
    is_blocked = models.BooleanField(
        'Заблокирован?',
        default=False)
    is_deleted = models.BooleanField(
        'Удалён?',
        default=False)
    is_confirm = models.BooleanField(
        'Подтвержден?',
        default=False)

    access_table = models.BooleanField(
        'Доступ к таблице',
        default=False)
    access_admin = models.BooleanField(
        'Доступ к панели управления',
        default=False)
    access_schedule = models.BooleanField(
        'Доступ к графикам работы',
        default=False)
    access_webinar = models.BooleanField(
        'Доступ к графику вебинаров',
        default=False)

    datedel = models.DateField(
        'Дата удаления',
        blank=True,
        null=True)
    created = models.DateTimeField(
        'Создан',
        auto_now_add=True,
        null=True)
    updated = models.DateTimeField(
        'Обновлён',
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


class AmoCRMContacts(models.Model):
    contact_id = models.IntegerField(
        'ID контакта',
        blank=True,
        null=True,
        default='')

    email = models.EmailField(
        'Почта',
        unique=False)

    phone = models.CharField(
        'Телефон',
        max_length=15,
        unique=False)

    name = models.CharField(
        'Имя',
        max_length=60,
        unique=False)

    temp = models.CharField(
        'Temp',
        max_length=10,
        default='')

    country = models.CharField(
        'Страна',
        max_length=30,
        default='')

    def __str__(self):
        return self.contact_id

    def save(self, *args, **kwargs):
        super().save()

    class Meta:
        db_table = 'AmoCRM Contacts'


class AmoCRMDeals(models.Model):
    contact_id = models.IntegerField(
        'ID контакта',
        default=0)

    email = models.EmailField(
        'Почта',
        unique=False)

    phone = models.CharField(
        'Телефон',
        max_length=30,
        default='')

    created_at = models.CharField(
        'Дата и время создания',
        max_length=30,
        default='')

    update_at = models.CharField(
        'Дата и время обновления',
        max_length=30,
        default='')

    price = models.IntegerField(
        'Бюджет',
        default=0)

    quantity = models.IntegerField(
        'Количество покупок',
        default=1)

    status = models.CharField(
        'Статус сделки',
        max_length=40,
        default='')

    deal_id = models.CharField(
        'ID сделки',
        max_length=20,
        default=0)

    payment_type = models.CharField(
        'Внешний идентификатор способа оплаты',
        max_length=40,
        default='')

    offer_id = models.CharField(
        'ID продукта',
        max_length=20,
        default=0)

    reason = models.CharField(
        'Причина отказа',
        max_length=30,
        default=0)

    def __str__(self):
        return self.deal_id

    def save(self, *args, **kwargs):
        super().save()

    class Meta:
        db_table = 'AmoCRM Deals'