from rest_framework import serializers
from myapp.models  import *

class Jenilserilizer(serializers.ModelSerializer):
    class Meta:
        model = Jenil
        fields = "__all__"