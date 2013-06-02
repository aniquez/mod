import logging
import re
import time
import datetime
import os
import hashlib
from django.conf import settings
from django.utils.functional import SimpleLazyObject

def context_processor(request):
    d = {
        'currenttime' : datetime.datetime.now(),
        'static_path' : settings.STATIC_PATH,
        'default_title' : settings.SITE_TITLE,
        'default_description' : settings.SITE_DESCRIPTION,
        'default_keywords' : settings.SITE_KEYWORDS,
        'default_site_name' : settings.SITE_NAME,
        'default_site_url' : settings.SITE_URL
    }
    return d
