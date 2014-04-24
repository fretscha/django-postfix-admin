#models.py
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

class Domain(models.Model):
    TRANSPORT_CHOICES = [(x, x) for x in ('virtual', 'relay', 'smtp')]
    domain = models.CharField(max_length=127, db_index=True)
    description = models.CharField(max_length=255, default='', blank=True)
    aliases = models.IntegerField(default=0)
    mailboxes = models.IntegerField(default=0)
    maxquota = models.IntegerField(default=0)
    quota = models.IntegerField(default=0)
    transport = models.CharField(max_length=8, choices=TRANSPORT_CHOICES, default='virtual')
    backupmx = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return "{0}".format(self.domain,)

    class Meta:
        db_table = 'domain'
        verbose_name_plural = "domain"
        verbose_name_plural = "domains"
        ordering = ['domain']


class Alias(models.Model):
    address = models.CharField(max_length=255, db_index=True)
    goto = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

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


class Mailbox(models.Model):
    domain = models.ForeignKey(Domain)
    username = models.EmailField(max_length=254, db_index=True)
    password = models.CharField(max_length=98)
    name = models.CharField(max_length=64)
    maildir = models.CharField(max_length=255)
    quota = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('mailbox_detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return "{0}, {1}".format(self.username, self.name)

    class Meta:
        db_table = 'mailbox'
        verbose_name_plural = "mailbox"
        verbose_name_plural = "mailboxes"
        ordering = ['domain', 'username']

class Vacation(models.Model):
    email = models.ForeignKey(Mailbox)
    subject = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    cache = models.CharField(max_length=255)
    domain = models.ForeignKey(Domain)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return "{0}, {1}".format(self.email, self.active)

    class Meta:
        db_table = 'vacation'
        verbose_name_plural = "vacation"
        verbose_name_plural = "vacations"
        ordering = ['email']
