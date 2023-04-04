import json
from datetime import datetime


from rest_framework.decorators import api_view
from rest_framework.response import Response

from order_details.models import OrderDetails


SUCESS = 'Sucess'
FAIL = 'Fail'


#API Functions
@api_view(['GET'])
def getOrders(_, pk):
    #TODO: Check authenticated user using JWT
    #TODO: Check if authenticated user is allowed to get order the data
    orders = {}

    if OrderDetails.object.filter(productId=pk).exists():
        orders = OrderDetails.object.filter(productId=pk).values()    

    return Response({'message': SUCESS, 'orders': orders})


@api_view(['PUT'])
def updateOrders(request):
    #TODO: Check authenticated user using JWT

    data = data = request.data

    if not data.__contains__('ids'):
        return Response({'message': FAIL}, 400)
    
    #TODO: Check if authenticated user is allowed to update the order data
    for id in data['ids']:
        if OrderDetails.object.filter(pk=id).exists():
            orderDetails =  OrderDetails.object.get(pk=id)
            orderDetails.shipedDate = datetime.now()
            OrderDetails.object.save(orderDetails)
    
    return Response({'message': SUCESS}, 200)

    