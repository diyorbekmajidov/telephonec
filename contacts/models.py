from django.db import models
from django.core.validators import RegexValidator
import json 


phone_regex = RegexValidator(
    regex=r'^\+998\d{9}$', 
    message="Phone number must be in the format: '+998XXXXXXXXX'."
)

class PersonContact(models.Model):
    full_name = models.CharField(blank=False, null=True, max_length=56)
    phone_number = models.CharField(
        max_length=13, 
        validators=[phone_regex], 
        unique=True
    )

    STATUS_METHODS = [
        ("1", 'Sektor Rahbar'),
        ("2", 'Aparat hodim'),
        ("3", 'Boshqa')
    ]
    status = models.CharField(max_length=20, choices=STATUS_METHODS, default=3)
    service_number = models.CharField(blank=False, null=True, max_length=56)
    position = models.CharField(max_length=56)
    own_number = models.CharField(max_length=56)
    home_number = models.CharField(max_length=56)

    date_created = models.DateField(auto_now_add=True)
    date_update   = models.DateField(auto_now=True)

    def __str__(self):
        return self.full_name

def get_district():
    with open('main.json', "r") as file:
        data = json.load(file)
    return [(i['id'] ,i["name"]) for i in data]

class SectorLeader(models.Model):

    name = models.CharField(max_length=56)
    district = models.CharField(max_length=20, choices=get_district())

    def __str__(self):
        return self.name