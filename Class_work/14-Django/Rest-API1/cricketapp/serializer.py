from rest_framework import serializers
from cricketapp.models import *


class cricketdeptserializer(serializers.ModelSerializer):
    class Meta:
        model = CricketDept
        fields = "__all__"

class cricketserializer(serializers.ModelSerializer):
    class Meta:
        model = Cricketdetalis
        fields = "__all__"
        depth = 1

    