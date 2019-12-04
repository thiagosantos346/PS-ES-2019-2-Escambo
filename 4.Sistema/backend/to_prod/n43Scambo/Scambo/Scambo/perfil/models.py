from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)
from django.conf import settings
from django.core import validators
import re

class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        'Nome de usuário', max_length=30, unique=True,
        validators=[
            validators.RegexValidator(re.compile('^[\w.@+-]+$'),
            'Somente letras, números, ou seguintes caracteres: @/./+/-/_- )',
            'invalid'
        )]
    )
    last_name = models.CharField(max_length=48)
    first_name = models.CharField(max_length=32)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=32)
    date_created = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=48)
    email_active = models.BooleanField('E-mail confirmado?', blank=True, default=False)

    is_staff = models.BooleanField(
        ('staff status'),
        default=False,
        help_text=('Designates whether the user can log into this admin site.'),
    )

    is_active = models.BooleanField(
        ('active'),
        default=True,
        help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )


    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.first_name or sefl.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return(self)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'


class UserAvatar(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to="User-avatar-images", null=True
    )
    thumbnail = models.ImageField(
        upload_to="User_avatar_thumbnails", null=True
    )
    slug = models.SlugField(max_length=48)

    def natural_key(self):
        return (self.slug)



class PasswordReset(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='User',
        related_name='resets', on_delete=models.CASCADE
    )
    key = models.CharField('Chave', max_length=100, unique=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    confirmed = models.BooleanField('Confirmado?', default=False, blank=True)

    def __str__(self):
        return '{0} em {1}'.format(self.user, self.created_at )
    
    class Meta:
        verbose_name = 'Nova Senha'
        verbose_name_plural = 'Novas senhas'
        ordering = ['-created_at']