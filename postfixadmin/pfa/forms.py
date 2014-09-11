from __future__ import absolute_import

from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit

from . import models


class DomainForm(forms.ModelForm):

    class Mata:
        fields = ('domain', 'mailboxes',)
