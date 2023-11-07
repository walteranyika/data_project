import json
import os.path

from django.core.management import BaseCommand

from data_project import settings
from main_app.models import Employee

records = []


class Command(BaseCommand):
    help = "Populates the db with some fake data"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('Started populating the db')
        )

        with open(os.path.join(settings.BASE_DIR, "data.json")) as file:
            data = json.load(file)
            for record in data:
                Employee.objects.create(
                    name=record["name"], email=record["email"], dob=record["dob"], salary=round(record["salary"]), disabled=record["disabled"])

        self.stdout.write(
            self.style.SUCCESS('Completed populating the db')
        )
