from rest_framework import serializers
from myapp.models import *

class Doctorserializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = "__all__"