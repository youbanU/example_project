from django.db import transaction

from demo.models import Person
from demo.models import Address


def person_create_(data):
    try:
        with transaction.atomic():
            address = data.pop('address')
            user_addresses = []
            for addr in address:
                user_addresses.append(Address.objects.create(**addr))

            create_person = Person.objects.create(**data)
            create_person.address.set(user_addresses)
            return create_person
    except Exception as e:
        return e


def person_update_(update_person, data):
    try:
        with transaction.atomic():
            address = data.pop('address')
            print('1')
            user_addresses = []
            # update_person.address.remove(address)
            # update_person.address.filter(address_set__person=update_person).delete()
            print('2')
            for addr in address:
                print('3')
                user_addresses.append(Address.objects.create(**addr))
            for key, value in data.items():
                print('4')
                setattr(update_person, key, value)
            print('5')
            update_person.save()
            update_person.address.set(user_addresses)
            return update_person
    except Exception as e:
        return e
