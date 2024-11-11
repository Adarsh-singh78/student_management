from django.core.management.base import BaseCommand
from faker import Faker
from home.models import student
class Command(BaseCommand):
    
    def handle(self,*args,**kwargs):
        fk=Faker()
        mob=fk.msisdn()[:10]
        while  not mob.startswith(('6','7','8','9')):
            mob=fk.msisdn()[:10]
        student.objects.create(
            name=fk.name(),
            email=fk.email(),
            mobile_no=mob
        )
        print("successfully added one")