from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
import json 

phone_regex = RegexValidator(
    regex=r'^\+998\d{9}$', 
    message="Phone number must be in the format: '+998XXXXXXXXX'."
)

def get_district():
    with open('main.json', "r") as file:
        data = json.load(file)
    return [(str(i['id']) ,i["name"]) for i in data]

class Permission(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    district = models.CharField(max_length=200, choices=get_district(), null=True, blank=True)

    can_add_user = models.BooleanField(default=False)
    can_edit_user = models.BooleanField(default=False)
    can_delete_user = models.BooleanField(default=False)
    can_view_all = models.BooleanField(default=False)  # for city admin

    def get_district_name(self): #this function get district name
        district_dict = dict(get_district())
        return district_dict.get(self.district, 'Tuman topilmadi')

    def is_city_admin(self):
        return self.district is None  # Tuman belgilangan bo'lmasa → Shahar admin

    def __str__(self):
        return f"{self.user.username} ({self.get_district_name() if self.district else 'City Admin'})"



class Management(models.Model): 
    class ManagementType(models.TextChoices):
        SEKTOR_RAHBAR = "Sektor Rahbar", "Sektor Rahbar"
        BOSHQARMA = "Boshqarma", "Boshqarma"

    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(
        max_length=50,
        choices=ManagementType.choices, 
        default=ManagementType.BOSHQARMA 
    )

    def __str__(self):
        return self.name

class Contact(models.Model):
    class StatusChoices(models.TextChoices):
        SEKTOR_RAHBAR = "Sektor Rahbar", "Sektor Rahbar"
        APARAT_HODIM = "Aparat hodim", "Aparat hodim"
        BOSHQARMA = "Boshqarma", "Boshqarma"

    full_name = models.CharField(max_length=56, blank=False, null=False)
    phone_number = models.CharField(max_length=13, validators=[phone_regex], unique=True)
    own_number = models.CharField(max_length=13, validators=[phone_regex], unique=True)
    status = models.CharField(
        max_length=20, choices=StatusChoices.choices,  # Enum'dan foydalanamiz
        default=StatusChoices.BOSHQARMA  # Default qiymat
    )
    management = models.ForeignKey(
        Management, on_delete=models.SET_NULL, null=True, blank=True, related_name="employees"
    )

    birthday = models.DateField()
    service_number = models.CharField(max_length=56, blank=True, null=True)
    position = models.CharField(max_length=56, blank=False, null=False)
    home_number = models.CharField(max_length=56, blank=True, null=True)

    district = models.CharField(max_length=200, choices=get_district())

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.status == "3" and not self.management:
            raise ValidationError({"management": "Boshqarma xodimi uchun boshqarma tanlanishi shart!"})
        if self.status == "1" and not self.management:
            raise ValidationError({"management": "Sektor Rahbar xodimi uchun sektor tanlanishi shart!"})
        
    def __str__(self):
        return f"{self.full_name} - {self.position} ({self.status})-{self.management}"
    