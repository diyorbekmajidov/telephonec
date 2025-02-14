from rest_framework import serializers
from .models import *
class ManagementSerializers(serializers.ModelSerializer):
    class Meta:
        model = Management
        fields = "__all__"
        