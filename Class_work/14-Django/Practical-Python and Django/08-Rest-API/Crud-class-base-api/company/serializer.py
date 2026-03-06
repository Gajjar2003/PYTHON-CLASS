from rest_framework import serializers
from company.models import *

class Deptserializer(serializers.ModelSerializer):
    class Meta:
        model = Dept
        fields = "__all__"


class Empserializer(serializers.ModelSerializer):
    class Meta:
        model = Emp
        fields = "__all__"
        depth = 1