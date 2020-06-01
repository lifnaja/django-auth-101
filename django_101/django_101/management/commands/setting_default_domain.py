from django.conf import settings
from django.contrib.sites.models import Site
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *arg, **kwarg):
        try:
            site = Site.objects.get(pk=settings.SITE_ID)
            site.domain = settings.DEFAULT_DOMAIN
            site.name = 'Default Domain'
            site.save()
        except ObjectDoesNotExist:
            pass
