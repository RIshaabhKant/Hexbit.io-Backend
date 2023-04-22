from rest_framework import serializers
from shipper.models import Shipper


class ShipperSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shipper
        fields = '__all__'

