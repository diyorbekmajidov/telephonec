from rest_framework import serializers
from .models import *
class ManagementSerializers(serializers.ModelSerializer):
    class Meta:
        model = Management
        fields = "__all__"
        

class ContactSerializers(serializers.ModelSerializer):
    district_display = serializers.SerializerMethodField()

    class Meta:
        model = Contact
        fields = ['id', 'full_name', 'phone_number', 'own_number', 'status', 'management',
                  'service_number', 'position', 'home_number', 'district', 'district_display']

    def get_district_display(self, obj):
        district_dict = dict(get_district())  # District nomlarini olish
        return district_dict.get(obj.district, "Tuman topilmadi")  # ID o‘rniga matn qaytarish

