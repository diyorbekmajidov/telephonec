from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import json 

phone_regex = RegexValidator(
    regex=r'^\+998\d{9}$', 
    message="Phone number must be in the format: '+998XXXXXXXXX'."
)

def get_district():
    with open('main.json', "r") as file:
        data = json.load(file)
    return [(str(i['id']) ,i["name"]) for i in data]

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Permission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    can_add_user = models.BooleanField(default=False)
    can_view_own_district = models.BooleanField(default=True)
    can_view_all = models.BooleanField(default=False)

    def __str__(self):
        return f"Permissions for {self.role.name}"

class Management(models.Model): 
    STATUS_METHODS = [
        ("1", 'Sektor Rahbar'),
        ("3", 'Boshqarma')
    ]
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(choices=STATUS_METHODS, max_length=50)

    def __str__(self):
        return self.name

class Contact(models.Model):
    full_name = models.CharField(max_length=56, blank=False, null=False)
    phone_number = models.CharField(max_length=13, validators=[phone_regex], unique=True)
    own_number = models.CharField(max_length=13, validators=[phone_regex], unique=True)

    STATUS_METHODS = [
        ("1", 'Sektor Rahbar'),
        ("2", 'Aparat hodim'),
        ("3", 'Boshqarma')
    ]
    status = models.CharField(max_length=20, choices=STATUS_METHODS, default="3")
    management = models.ForeignKey(
        Management, on_delete=models.SET_NULL, null=True, blank=True, related_name="employees"
    )

    service_number = models.CharField(max_length=56, blank=True, null=True)
    position = models.CharField(max_length=56, blank=False, null=False)
    home_number = models.CharField(max_length=56, blank=True, null=True)

    district = models.CharField(max_length=200, choices=get_district())
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.status == "3" and not self.management:
            raise ValidationError({"management": "Boshqarma xodimi uchun boshqarma tanlanishi shart!"})
        
    def __str__(self):
        return f"{self.full_name} - {self.position} ({self.status})"