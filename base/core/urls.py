from django.conf.urls import patterns, url, include

from fhurl import fhurl
from core.forms import *

urlpatterns = patterns('core.views',
    #url for testing flat pages
    url(r'^html/(?P<filename>[\w-]+).html$', 'show_html'),

)
