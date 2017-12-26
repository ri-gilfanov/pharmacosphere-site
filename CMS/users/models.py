from django.db import models
from django.db.models.signals import post_delete
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from core.model_functions import del_img_at_obj_del, del_img_at_obj_change
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class AbsUser(models.Model):
    last_name = models.CharField('фамилия', blank=True, max_length=30,)
    first_name = models.CharField('имя', blank=True, max_length=30)
    patronymic = models.CharField('отчество', blank=True, max_length=30)
    text = RichTextUploadingField('о себе', blank=True, config_name='dflt_config')
    image_50x50 = ImageSpecField(
        source='image',
        processors=[ResizeToFill(50, 50)],
        format='PNG',
        options={'quality': 60},
    )
    birth_date = models.DateField('дата рождения', blank=True, null=True)

    def get_full_name(self):
        first_name = self.first_name
        patronymic = self.patronymic
        last_name = self.last_name
        if first_name and patronymic and last_name:
            return '%s %s %s' % (first_name, patronymic, last_name)
        elif first_name and last_name:
            return '%s %s' % (first_name, last_name)
        elif first_name and patronymic:
            return '%s %s' % (first_name, patronymic)
        else:
            return first_name or last_name or patronymic or self.pk

    def get_reverse_name(self):
        first_name = self.first_name
        patronymic = self.patronymic
        last_name = self.last_name
        if first_name and patronymic and last_name:
            return '%s, %s %s' % (last_name, first_name, patronymic)
        elif first_name and last_name:
            return '%s, %s' % (last_name, first_name)
        elif first_name and patronymic:
            return '%s %s' % (first_name, patronymic)
        else:
            return first_name or last_name or patronymic or self.pk

    def get_reverse_initials(self):
        first_name = self.first_name
        patronymic = self.patronymic
        last_name = self.last_name
        if first_name and patronymic and last_name:
            return '%s.%s. %s' % (first_name[0], patronymic[0], last_name)
        elif first_name and last_name:
            return '%s. %s' % (first_name[0], last_name)
        elif first_name and patronymic:
            return '%s.%s.' % (first_name[0], patronymic[0])
        else:
            return first_name or last_name or patronymic or self.pk

    def get_short_name(self):
        first_name = self.first_name
        patronymic = self.patronymic
        if first_name and patronymic:
            return '%s %s' % (first_name, patronymic)
        else:
            return first_name or patronymic or self.pk

    class Meta:
        abstract = True


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        """
        Creates and saves a User with the given username and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        username = self.model.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)


class User(AbsUser, AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        'имя пользователя',
        error_messages={
            'unique': 'Пользователь с таким именем уже существует.',
        },
        help_text='Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.',
        max_length=150,
        validators=[username_validator],
        unique=True,
    )
    image = models.ImageField('фотография', blank=True, upload_to='users/pub/%Y/%m/%d/')
    date_joined = models.DateTimeField(default=timezone.now, verbose_name='дата регистрации')
    is_active = models.BooleanField(
        'активный',
        default=True,
        help_text='Отметьте, если пользователь должен считаться активным. Уберите эту отметку вместо удаления учётной записи.',
    )
    is_staff = models.BooleanField(
        'статус персонала',
        default=False,
        help_text='Отметьте,\
            если пользователь может входить в административную часть сайта.',
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def save(self, *args, **kwargs):
        del_img_at_obj_change(post_object=self)
        super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        ordering = ('last_name', 'first_name', 'patronymic',)
        verbose_name = 'профиль пользователя'
        verbose_name_plural = 'профили пользователей'


post_delete.connect(del_img_at_obj_del, User)


class UserDraft(AbsUser):
    image = models.ImageField('фотография', blank=True, upload_to='users/sug/%Y/%m/%d/')
    user = models.OneToOneField(User, models.CASCADE, verbose_name='профиль')
    last_modified = models.DateTimeField('отредактировано', auto_now=True)
    is_ready = models.BooleanField('готово для размещения', default=True)
    is_published = models.BooleanField('опубликовано', default=False)

    def save(self, *args, **kwargs):
        del_img_at_obj_change(post_object=self)
        super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        ordering = ('is_published', 'last_modified',)
        verbose_name = 'черновик профиля'
        verbose_name_plural = 'черновики профилей'


post_delete.connect(del_img_at_obj_del, UserDraft)
