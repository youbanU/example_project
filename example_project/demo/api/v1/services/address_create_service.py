from django.db import transaction

from demo.models import Address


def address_create_(data):
    try:
        with transaction.atomic():
                create_address = Address.objects.create(**data)
        return create_address
        return create_address
    except Exception as e:
        return e


def address_update_(update_address, data):
    for key, value in data.items():
        setattr(update_address, key, value)
    update_address.save()
    return update_address
