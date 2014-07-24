# serializer.py

from rest_framework import serializers

from pfa import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'date_of_birth',
            'is_admin',
            'is_active',
            'is_superuser',
            'last_login',
            'date_joined')


class DomainSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Domain
        fields = (
            'id',
            'domain',
            'description',
            'aliases',
            'mailboxes',
            'quota',
            'transport',
            'backupmx',
            'created_on',
            'modified_on',
            'active')


class AliasSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Alias
        fields = (
            'id',
            'address',
            'goto',
            'domain',
            'created_on',
            'modified_on',
            'active')


class MailboxSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Mailbox
        fields = (
            'id',
            'domain',
            'username',
            'password',
            'name',
            'maildir',
            'quota',
            'created_on',
            'modified_on',
            'active')


class VacationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Vacation
        fields = (
            'id',
            'email',
            'subject',
            'body',
            'cache',
            'domain',
            'created_on',
            'modified_on',
            'active')


class LogSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Log
        fields = (
            'id',
            'timestamp',
            'username',
            'domain',
            'action',
            'data')
