from rest_framework import serializers
from myapp.models import *


class Subjectserializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"

class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        depth = 1