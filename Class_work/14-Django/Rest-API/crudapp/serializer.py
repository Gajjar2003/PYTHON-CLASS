from rest_framework import serializers
from crudapp.models import *

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields = "__all__"

