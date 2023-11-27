from django.core.management import BaseCommand

from catalog.models import Category, Product
from django.db.models import Max


class Command(BaseCommand):

    def handle(self, *args, **options):

        Category.objects.all().delete()


        category_list = [
            {'category_name': 'Фрукт'},
            {'category_name': 'Овощ'},
        ]

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )
        Category.objects.bulk_create(category_for_create)

