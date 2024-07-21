from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Populate database with data"
    def handle(self, *args, **options):
        pass