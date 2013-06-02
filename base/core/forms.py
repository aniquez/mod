from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import authenticate

import random
import datetime,time
import uuid
import re
import hashlib

from core.models import *
from fhurl import RequestForm, RequestModelForm
from customforms.ajaxfield import AjaxField

class SampleForm(forms.Form):
    employee = forms.CharField(required=True)
    ufile = forms.FileField(required=True)

    def __init__(self, *args, **kwargs):
        super(SampleForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        d = self.cleaned_data.get
        return None

    def clean_employee(self):
        if self.cleaned_data.get('employee') not in ['devendra', 'rane']:
            raise forms.ValidationError("Please Enter Correct Employee-ID")
        else:
            return self.cleaned_data.get('employee').title()
