from rest_framework import serializers
from myapp.models import *

class techerserializer(serializers.ModelSerializer):
    class Meta:
        model = Techer
        fields = "__all__"