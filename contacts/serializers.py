from rest_framework import serializers
from .models import *
class ManagementSerializers(serializers.ModelSerializer):
    class Meta:
        model = Management
        fields = "__all__"
        

class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"