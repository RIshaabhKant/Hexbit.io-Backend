from rest_framework import serializers

from order_details.models import OrderDetails
from order.serializers import OrderSerializer


class OrderDetailsSerializer(serializers.ModelSerializer):
    
    
    order = OrderSerializer()
    class Meta:
        model = OrderDetails
        fields = ['order', 'price', 'quantity', 'discount', 'total', 'shipedDate', 'billDate', 'fullfilled']

