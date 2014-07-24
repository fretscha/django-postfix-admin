# views.py
from rest_framework import generics

from . import serializer
from pfa import models


class UserList(generics.ListAPIView):
    model = models.User
    serializer_class = serializer.UserSerializer


class DomainListOrCreate(generics.ListCreateAPIView):
    model = models.Domain
    serializer_class = serializer.DomainSerializer


class DomainDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.Domain
    serializer_class = serializer.DomainSerializer


class AliasListOrCreate(generics.ListCreateAPIView):
    model = models.Alias
    serializer_class = serializer.AliasSerializer


class AliasDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.Alias
    serializer_class = serializer.AliasSerializer


class MailboxListOrCreate(generics.ListCreateAPIView):
    model = models.Mailbox
    serializer_class = serializer.MailboxSerializer


class MailboxDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.Mailbox
    serializer_class = serializer.MailboxSerializer


class VacationListOrCreate(generics.ListCreateAPIView):
    model = models.Vacation
    serializer_class = serializer.VacationSerializer


class VacationDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.Vacation
    serializer_class = serializer.VacationSerializer


class LogListOrCreate(generics.ListCreateAPIView):
    model = models.Log
    serializer_class = serializer.LogSerializer


class LogDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.Log
    serializer_class = serializer.LogSerializer
