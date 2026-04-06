from rest_framework import serializers
from myapp.models import *

class moblieserlizer(serializers.ModelSerializer):
    class Meta:
        model = Moblie
        fields = "__all__"