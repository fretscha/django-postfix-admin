# views.py
from django.http import Http404

from rest_framework import generics

from . import serializer
from pfa import models
from rest_framework.permissions import IsAdminUser


class UserList(generics.ListAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializer.UserSerializer
    permission_classes = (IsAdminUser,)
    paginate_by = 100


class DomainListOrCreate(generics.ListCreateAPIView):
    queryset = models.Domain.objects.all()
    serializer_class = serializer.DomainSerializer
    permission_classes = (IsAdminUser,)
    paginate_by = 100


class DomainDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Domain.objects.all()
    serializer_class = serializer.DomainSerializer


class MailboxListOrCreate(generics.ListCreateAPIView):
    queryset = models.Mailbox.objects.all()
    serializer_class = serializer.MailboxSerializer
    permission_classes = (IsAdminUser,)
    paginate_by = 100


class MailboxDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Mailbox.objects.all()
    serializer_class = serializer.MailboxSerializer


class AliasListOrCreate(generics.ListCreateAPIView):
    queryset = models.Alias.objects.all()
    serializer_class = serializer.AliasSerializer
    permission_classes = (IsAdminUser,)
    paginate_by = 100


class AliasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Alias.objects.all()
    serializer_class = serializer.AliasSerializer


class VacationListOrCreate(generics.ListCreateAPIView):
    queryset = models.Vacation.objects.all()
    serializer_class = serializer.VacationSerializer


class VacationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Vacation.objects.all()
    serializer_class = serializer.VacationSerializer


class LogList(generics.ListAPIView):
    queryset = models.Log.objects.all()
    serializer_class = serializer.LogSerializer


class LogDetail(generics.RetrieveAPIView):
    queryset = models.Log.objects.all()
    serializer_class = serializer.LogSerializer
