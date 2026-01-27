from rest_framework import serializers
from companyapp.models import *


class Deptserializer(serializers.ModelSerializer):
    class Meta:
        model = Dept
        fields = "__all__"


class Empserializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
        depth =1