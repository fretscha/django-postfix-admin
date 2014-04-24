#views.py
from rest_framework import generics

from .serializer import DomainSerializer, AliasSerializer, MailboxSerializer, VacationSerializer, LogSerializer
from pfa.models import Domain, Alias, Mailbox, Vacation, Log

class DomainListOrCreate(generics.ListCreateAPIView):
    model = Domain
    serializer_class = DomainSerializer

class DomainDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Domain
    serializer_class = DomainSerializer


class AliasListOrCreate(generics.ListCreateAPIView):
    model = Alias
    serializer_class = AliasSerializer

class AliasDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Alias
    serializer_class = AliasSerializer


class MailboxListOrCreate(generics.ListCreateAPIView):
    model = Mailbox
    serializer_class = MailboxSerializer

class MailboxDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Mailbox
    serializer_class = MailboxSerializer


class VacationListOrCreate(generics.ListCreateAPIView):
    model = Vacation
    serializer_class = VacationSerializer

class VacationDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Vacation
    serializer_class = VacationSerializer


class LogListOrCreate(generics.ListCreateAPIView):
    model = Log
    serializer_class = LogSerializer

class LogDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Log
    serializer_class = LogSerializer

