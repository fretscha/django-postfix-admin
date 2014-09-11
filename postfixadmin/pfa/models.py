# models.py
from os.path import normpath, join

from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

import logging

import datetime


def now_plus(delta_days=3650):
    return datetime.now() + datetime.timedelta(days=delta_days)

logger = logging.getLogger(__name__)


class Domain(models.Model):
    TRANSPORT_CHOICES = [(x, x) for x in ('virtual', 'relay', 'smtp')]
    domain = models.CharField(blank=False, max_length=127, unique=True)
    description = models.CharField(max_length=255, default='', blank=True)
    aliases = models.IntegerField(blank=False, default=0)
    mailboxes = models.IntegerField(blank=False, default=0)
    maxquota = models.IntegerField(blank=False, default=0)
    quota = models.IntegerField(blank=False, default=0)
    transport = models.CharField(
        max_length=8, choices=TRANSPORT_CHOICES, default='virtual')
    backupmx = models.BooleanField(blank=False, default=False)
    created = models.DateTimeField(blank=False, auto_now_add=True)
    modified = models.DateTimeField(blank=False, auto_now=True)
    expired = models.DateTimeField(blank=False, default=now_plus())
    active = models.BooleanField(blank=False, default=True)

    def __unicode__(self):
        return "{0}".format(self.domain,)

    def get_absolute_url(self):
        return reverse('pfa:domain:detail', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'domain'
        verbose_name_plural = "domain"
        verbose_name_plural = "domains"
        ordering = ['domain']


class DomainPerm(models.Model):
    DOMAIN_PERM_CHOICES = [(x, x) for x in ('superuser', 'domadmin', 'user')]
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="domain_perm_user")
    domain = models.ForeignKey(Domain, related_name="domain_perm_domain")
    type = models.CharField(
        blank=False, max_length=9, choices=DOMAIN_PERM_CHOICES, default='user')

    def __unicode__(self):
        return "{0} is {1} for {2}".format(self.user, self.type, self.domain,)


class UserManager(BaseUserManager):

    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
                                password=password,
                                date_of_birth=date_of_birth
                                )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    perms = models.ManyToManyField(DomainPerm, related_name='user_doamin_perm')
    first_name = models.CharField(max_length=32, default='', blank=True)
    last_name = models.CharField(max_length=32, default='', blank=True)
    email = models.EmailField(
        verbose_name='email address', max_length=255, unique=True)
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(blank=False, auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_perms(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Mailbox(models.Model):
    domain = models.ForeignKey(Domain, related_name="maiilbox_domain")
    email = models.EmailField(blank=False, max_length=255)
    password = models.CharField(blank=False, max_length=255)
    maildir = models.CharField(
        blank=False, max_length=255, default='get_default_maildir()')
    quota = models.IntegerField(blank=False, default=0)
    created_on = models.DateTimeField(blank=False, auto_now_add=True)
    modified_on = models.DateTimeField(blank=False, auto_now=True)

    def get_absolute_url(self):
        return reverse('mailbox_detail', kwargs={'pk': self.pk})

    def get_default_maildir(self):
        return normpath(join(settings.PFA_DEFAULT_MAILDIR, self.email))

    def __unicode__(self):
        return "{0}, {1}".format(self.email, self.active)

    class Meta:
        db_table = 'mailbox'
        verbose_name_plural = "mailbox"
        verbose_name_plural = "mailboxes"
        ordering = ['domain', 'email']


class Alias(models.Model):
    address = models.CharField(blank=False, max_length=255, unique=True)
    goto = models.CharField(max_length=255)
    domain = models.ForeignKey(
        Domain, blank=False, related_name='alias_domain')
    created_on = models.DateTimeField(blank=False, auto_now_add=True)
    modified_on = models.DateTimeField(blank=False, auto_now=True)
    active = models.BooleanField(blank=False, default=True)

    def __unicode__(self):
        return "{0} -> {1}".format(self.address, self.goto)

    class Meta:
        db_table = 'alias'
        verbose_name_plural = "alias"
        verbose_name_plural = "aliases"
        ordering = ['domain', 'address']


class Log(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    username = models.CharField(max_length=63)
    domain = models.CharField(max_length=63)
    action = models.CharField(max_length=255)
    data = models.CharField(max_length=255)

    def __unicode__(self):
        return "{0}".format(self.timestamp, self.username, self.action)

    class Meta:
        db_table = 'log'
        verbose_name_plural = "log"
        verbose_name_plural = "logs"
        ordering = ['timestamp']


class Vacation(models.Model):
    email = models.ForeignKey(
        Mailbox, blank=False, related_name='vacation_email')
    subject = models.CharField(blank=False, max_length=255)
    body = models.CharField(blank=False, max_length=255)
    cache = models.CharField(max_length=255)
    domain = models.ForeignKey(
        Domain, blank=False,  related_name='vacation_domain')
    created_on = models.DateTimeField(blank=False, auto_now_add=True)
    modified_on = models.DateTimeField(blank=False, auto_now=True)
    active = models.BooleanField(blank=False, default=True)

    def __unicode__(self):
        return "{0}, {1}".format(self.email, self.active)

    class Meta:
        db_table = 'vacation'
        verbose_name_plural = "vacation"
        verbose_name_plural = "vacations"
        ordering = ['email']
