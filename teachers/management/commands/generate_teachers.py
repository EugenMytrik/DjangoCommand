from django.core.management.base import BaseCommand
from faker import Faker
from teachers.models import Teacher


class Command(BaseCommand):
    help = "Generate some data"

    def add_arguments(self, parser):
        parser.add_argument("count", type=int, nargs="?", default=100)

    def handle(self, *args, **kwargs):
        count = kwargs["count"]
        fake = Faker()

        for i in range(count):
            teacher = Teacher(
                job=fake.job(),
                name=fake.name(),
            )
            teacher.save()
