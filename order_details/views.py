from datetime import datetime
import json

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from order_details.models import OrderDetails
from order_details.serializers import OrderDetailsSerializer

from common.utility.authentication_service import get_user_for_request


SUCESS = 'Sucess'
FAIL = 'Fail'


#API Functions
@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def getOrders(request, pk):

    user = get_user_for_request(request)
    order_details = {}

    if OrderDetails.object.filter(product_id=pk, product__shop__userProfile=user).exists():
        _order_details = OrderDetails.object.filter(product_id=pk, product__shop__userProfile=user).all()
        serialised_order_details = OrderDetailsSerializer(_order_details, many=True)
        bytesString = json.dumps(serialised_order_details.data)
        order_details = json.loads(bytesString)

    return Response({'message': SUCESS, 'order_details': order_details})


@api_view(['PUT'])
@permission_classes([IsAuthenticated, ])
def updateOrders(request):

    user = get_user_for_request(request)
    data = data = request.data

    if not data.__contains__('ids'):
        return Response({'message': FAIL}, 400)
    
    for id in data['ids']:
        if OrderDetails.object.filter(pk=id, product__shop__userProfile=user).exists():
            orderDetails =  OrderDetails.object.get(pk=id, product__shop__userProfile=user)
            if  not orderDetails.shipedDate:
                orderDetails.shipedDate = datetime.now()
                OrderDetails.object.save(orderDetails)
    
    return Response({'message': SUCESS}, 200)

    