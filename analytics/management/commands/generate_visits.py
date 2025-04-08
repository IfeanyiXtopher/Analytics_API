import random
from django.core.management.base import BaseCommand
from faker import Faker

from analytics.models import Visit

###################################################################################################################################
class Command(BaseCommand):
    help = 'Generate 10,000 fake visit records'

    def handle(self, *args, **options):
        fake = Faker()
        visits = []
        device_choices = [choice[0] for choice in Visit.DEVICE_CHOICES]

        for _ in range(10000):
            visits.append(Visit(
                ip_address=fake.ipv4(),
                page_url=fake.url(),
                country=fake.country(),
                device_type=random.choice(device_choices)
            ))

        Visit.objects.bulk_create(visits)
        self.stdout.write(self.style.SUCCESS('Successfully generated 10,000 visits'))

