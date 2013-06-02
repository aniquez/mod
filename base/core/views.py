import datetime
import hashlib
import logging

from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from django.shortcuts import render_to_response, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.core import serializers
from django.forms.models import modelformset_factory
from django.forms.formsets import formset_factory
from django.contrib.auth import authenticate, login
from django.utils import simplejson
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from core.forms import *
from core.models import *
from customdb.customquery import sqltojson, sqltodict, executesql
from xl2python import Xl2Python

def show_html(request, filename):
    return render_to_response("core/%s.html" % (filename), { },
        context_instance=RequestContext(request)
    )
