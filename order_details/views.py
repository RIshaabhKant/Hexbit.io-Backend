from datetime import datetime


from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from order_details.models import OrderDetails

from common.utility.authentication_service import get_user_for_request


SUCESS = 'Sucess'
FAIL = 'Fail'


#API Functions
@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def getOrders(request, pk):

    user = get_user_for_request(request)
    orders = {}

    if OrderDetails.object.filter(product_id=pk, product__shop__userProfile=user).exists():
        orders = OrderDetails.object.filter(product_id=pk, product__shop__userProfile=user).values()    

    return Response({'message': SUCESS, 'orders': orders})


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

    