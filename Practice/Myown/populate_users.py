import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'Myown.settings')

import django
django.setup()

from Myapp.models import user
from faker import Faker

fakegen=Faker()

def populate(N=5):
    for entry in range(N):
        fake_name=fakegen.name().split()
        fake_first_name=fake_name[0]
        fake_last_name=fake_name[1]
        fake_e_mail=fakegen.email()

        users=user.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, e_mail=fake_e_mail)[0]

if __name__=='__main__':
    print("POPULATING DATABASES")
    populate(20)
    print("COMPLETE!")
