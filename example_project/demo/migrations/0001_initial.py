# Generated by Django 4.0.6 on 2022-10-02 18:06

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('address', models.CharField(default='', max_length=250, null=True)),
                ('street_number', models.CharField(blank=True, default='', max_length=30)),
                ('city', models.CharField(blank=True, default='', max_length=30)),
                ('state', models.CharField(blank=True, default='', max_length=30)),
                ('zip_code', models.CharField(blank=True, max_length=5, validators=[django.core.validators.RegexValidator('^[0-9+]', 'Only numeric characters')])),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('FEMALE', 'Female'), ('MALE', 'Male'), ('OTHER', 'Other')], default='FEMALE', max_length=12)),
                ('height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('phone_number', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('address', models.ManyToManyField(blank=True, related_name='person_address', to='demo.address')),
            ],
        ),
    ]
