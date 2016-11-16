from __future__ import unicode_literals, absolute_import
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core import validators
from django.contrib.auth import login
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from rest_framework.authtoken.models import Token


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom model user.
    """

    username = models.CharField(
        _('username'),
        max_length=30,
        unique=False,
        default=_('Username')
    )

    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    pro = models.ForeignKey("pro.Pro", blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def token(self):
        token, created = Token.objects.get_or_create(user=self)
        return token.key

    def get_short_name(self):
        "Returns the short name for the user."
        return self.email
