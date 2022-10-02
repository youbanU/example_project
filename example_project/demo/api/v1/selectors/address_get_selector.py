from demo.models import Address


def address_get_(qs_, user):
    address = qs_.get('address')
    city = qs_.get('city')
    state = qs_.get('state')

    if address:
        query_set = Address.objects.filter(address=address)
    elif city:
        query_set = Address.objects.filter(city=city)
    elif state:
        query_set = Address.objects.filter(state=state)
    else:
        query_set = Address.objects.all()

    return query_set