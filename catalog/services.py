from django.core.cache import cache

from catalog.models import Category
from config.settings import CACHE_ENABLED

def get_cached_data(_key):
    if CACHE_ENABLED:
        key = _key
        category_list = cache.get(key)
        if category_list is None:
            category_list = Category.objects.all()
            cache.get(key, category_list)
    else:
        category_list = Category.objects.all()