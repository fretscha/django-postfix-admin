from django.contrib.auth.models import User
from django.test import TestCase
from pfa import models


class DomainTestCase(TestCase):

    def setUp(self):
        self.superuser = User.objects.create(username='superuser')
        self.domadm1 = User.objects.create(username='domadm1')
        self.domadm2 = User.objects.create(username='domadm2')
