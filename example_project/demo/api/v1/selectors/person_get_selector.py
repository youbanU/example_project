from demo.models import Person


def person_get_(qs_, user):
    gender = qs_.get('gender')
    age = qs_.get('age')
    height = qs_.get('height')
    weight = qs_.get('weight')

    if gender:
        query_set = Person.objects.filter(gender=gender.upper())
    elif age:
        query_set = Person.objects.filter(age=age)
    elif height:
        query_set = Person.objects.filter(height=height)
    elif weight:
        query_set = Person.objects.filter(weight=weight)
    else:
        query_set = Person.objects.all()

    return query_set