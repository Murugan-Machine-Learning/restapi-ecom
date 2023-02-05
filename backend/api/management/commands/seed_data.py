from django.core.management.base import BaseCommand
from api.models import Country

class Command(BaseCommand):
    help = 'Seed the database with countries data'

    def handle(self, *args, **options):
        country_list = ['Uzbekistan', 'Russia', 'United States', 'India', 'Afganistan']
        for country_name in country_list:
            Country.objects.create(name=country_name)
        self.stdout.write(self.style.SUCCESS('Data seeded successfully'))
