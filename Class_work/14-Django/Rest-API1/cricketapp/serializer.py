from rest_framework import serializers
from cricketapp.models import *


class coachserializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = "__all__"


class cricketdeptserializer(serializers.ModelSerializer):
    class Meta:
        model = CricketDept
        fields = "__all__"
        
    def to_representation(self, instance):
        ret =  super().to_representation(instance)
        ret['coach'] = coachserializer(instance.coach).data
        return ret

class cricketserializer(serializers.ModelSerializer):
    class Meta:
        model = Cricketdetalis
        fields = "__all__"
     
    def to_representation(self, instance):
        ret =  super().to_representation(instance)
        ret['dept'] = cricketdeptserializer(instance.dept).data
        return ret

    