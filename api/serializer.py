#serializer.py
from rest_framework import serializers

from  pfa.models import Domain, Alias, Mailbox, Vacation, Log

class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ('id',
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
        model = Alias
        fields = ('id',
            'address',
            'goto',
            'domain',
            'created_on',
            'modified_on',
            'active')


class MailboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailbox
        fields = ('id',
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
        model = Vacation
        fields = ('id',
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
        model = Log
        fields = ('id',
            'timestamp',
            'username',
            'domain',
            'action',
            'data')
