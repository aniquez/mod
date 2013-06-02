from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import permalink
from django.contrib.auth.models import UserManager, AbstractBaseUser, BaseUserManager
from customdb.uuidfield import UUIDField
from django.core import serializers
from django.utils import timezone
import json, hashlib
import re

######### SOUTH HACKS ########
try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^tagging\.fields\.TagField"])
    add_introspection_rules([], ["^django_extensions\.db\.models\.AutoSlugField"])
    add_introspection_rules([], ["^customdb\.thumbs\.ImageWithThumbsField"])
except ImportError:
    pass
#############################

class UserManager(BaseUserManager):
    def create_user(self, email, username=None, password=None, first_name=""):
        """
        Creates and saves a User with the given email, username if given
        """
        if not email:
            raise ValueError('Users must have an email address')

        if not username:
            username = hashlib.md5(email).hexdigest()

        user = self.model(
            email = UserManager.normalize_email(email),
            username = username,
            first_name = first_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, first_name):
        """
        Creates and saves a superuser with the given email, username
        and password.
        """
        user = self.create_user(email,
            username = username,
            password = password,
            first_name = first_name,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    """Custom User Model"""

    GENDER_CHOICES = (
        (1, 'Male'),
        (2, 'Female'),
    )
    ROLE_CHOICES = (
        ('AUTHOR', 'Author'),
        ('REPORT', 'Report'),
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']

    email = models.EmailField(_('e-mail address'), max_length=255, blank=False, unique=True, db_index=True)
    username = models.CharField(_('username'), max_length=255, blank=False, unique=True, db_index=True) # If not in use, fill with md5 of email
    slug = models.SlugField(_('slug'), max_length=70)
    first_name = models.CharField(_('first name'), max_length=50, blank=True)
    middle_name = models.CharField(_('middle name'), max_length=50, blank=True)
    last_name = models.CharField(_('last name'), max_length=50, blank=True)

    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_superuser = models.BooleanField(_('superuser status'), default=False)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    role = models.CharField(_('role'), choices=ROLE_CHOICES, max_length=50)
    gender = models.PositiveSmallIntegerField(_('gender'), choices=GENDER_CHOICES, blank=True, null=True)
    mugshot = models.FileField(_('mugshot'), upload_to='mugshots', blank=True)
    extra = models.TextField(_('extra'), blank=True) #For all user data

    objects = UserManager()

    def __unicode__(self):
        return u"%s" % self.get_full_name()

    def get_full_name(self):
        return  re.sub(r' +',' '," ".join([self.first_name, self.middle_name, self.last_name]))

    def get_short_name(self):
        return self.first_name

    @property
    def ext(self):
        "Return extra parameters"
        return json.loads(self.extra)

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app 'app_label'?"
        return True

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    @permalink
    def get_absolute_url(self):
        return ('profile_detail', None, { 'username': self.username })
