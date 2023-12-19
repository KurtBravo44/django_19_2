
from django.db.models.signals import post_save
from django.dispatch import receiver

from catalog.models import Version


@receiver(post_save, sender=Version)
def set_current_version(updated, **kwargs):
    instance = kwargs['instance']
    if updated:
        Version.objects.all(current=False)
        instance(current=True)