import uuid

from django.core.validators import RegexValidator
from django.db import models

NUMERIC_VALIDATOR = RegexValidator(r'^[0-9+]', 'Only numeric characters')
GENDER_TYPE_CHOICE = (
    ('FEMALE', 'Female'),
    ('MALE', 'Male'),
    ('OTHER', 'Other')
)


# Create your models here.
class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address = models.CharField(default="", null=True, max_length=250)
    street_number = models.CharField(max_length=30, blank=True, default="")
    city = models.CharField(max_length=30, blank=True, default="")
    state = models.CharField(max_length=30, blank=True, default="")
    zip_code = models.CharField(max_length=5, validators=[
        NUMERIC_VALIDATOR], blank=True)

    @property
    def full_address(self):
        return self.address + ' ' + self.street_number + ' ' + self.city + ' ' + self.state


class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    age = models.IntegerField(blank=False)
    gender = models.CharField(choices=GENDER_TYPE_CHOICE, max_length=12, default="FEMALE")
    height = models.DecimalField(decimal_places=2, max_digits=5)
    weight = models.DecimalField(decimal_places=2, max_digits=5)
    phone_number = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    address = models.ManyToManyField(Address, related_name="person_address", blank=True)

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name
