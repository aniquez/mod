from django.core.management.base import NoArgsCommand, BaseCommand, CommandError
from django.conf import settings
import os

class Command(NoArgsCommand):
    args = '<poll_id poll_id ...>'
    help = 'Cleans static cache created by django compressor'

    def handle_noargs(self, **options):
        cache_dir = os.path.join(settings.COMPRESS_ROOT, settings.COMPRESS_OUTPUT_DIR)
        print "Deleting Django-Compressor Cache directory %s" % (cache_dir)
        command = 'rm -rf "%s"' % (cache_dir)
        os.system(command)
