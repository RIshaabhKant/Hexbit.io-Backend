import json

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from shipper.models import Shipper
from order.models import Order
from order_details.models import OrderDetails
from shipper.serializers import ShipperSerializer

from common.utility.authentication_service import get_user_for_request


SUCESS = 'Sucess'
FAIL = 'Fail'
TYPE = 'type'
SHIPPERS = 'shippers'
ORDER_ID = 'order_id'
TOTALCHECKPOINTS = 'totalCheckpoint'
CHECKPOINT = 'checkpoint'
CURRENTCHECKPOINT = 'currentCheckpoint'
TRACKINGURL = 'trackingUrl'
URLSTATUS = 'urlStatus'
COMPANYNAME = 'companyName'
UPDATE = 'update'


#API Functions
@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def getShipper(request, pk):

    user = get_user_for_request(request)

    if not OrderDetails.object.filter(product__shop__userProfile=user, order_id=pk).exists():
        return Response({'message': FAIL}, 404)
    
    order_details = OrderDetails.object.get(product__shop__userProfile=user, order_id=pk)

    if not order_details.order.shipper_id:
        return Response({'message': FAIL}, 404)
    
    serialised_shipper = ShipperSerializer(order_details.order.shipper)
    bytesString = json.dumps(serialised_shipper.data)
    shipper = json.loads(bytesString)


    return Response({'message': SUCESS, "shipper": shipper})


@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def createShipper(request):
    data = request.data

    if not data.__contains__(SHIPPERS):
        return Response({'message': FAIL}, 400)
    
    user = get_user_for_request(request)

    for shipper in data[SHIPPERS]:
        if not shipper.__contains__(TYPE) or not shipper.__contains__(ORDER_ID) or not shipper.__contains__(COMPANYNAME):
            return Response({'message': FAIL}, 400)
        
        if not OrderDetails.object.filter(product__shop__userProfile=user, order_id=shipper[ORDER_ID]).exists():
            return Response({'message': FAIL}, 404)
        
        order_details = OrderDetails.object.get(product__shop__userProfile=user, order_id=shipper[ORDER_ID])
        
        newshipper: Shipper
        
        if shipper[TYPE] == 0:
            #Small Scale Seller
            if not shipper.__contains__(TOTALCHECKPOINTS) or not shipper.__contains__(CURRENTCHECKPOINT) or not shipper.__contains__(CHECKPOINT):
                return Response({'message': FAIL}, 400)
            
            if shipper[TOTALCHECKPOINTS]<=0 or shipper[CURRENTCHECKPOINT]<=0 or not len(shipper[CHECKPOINT]) == shipper[TOTALCHECKPOINTS]:
                return Response({'message': FAIL}, 400)
            
            newshipper = Shipper.object.create_shipper(type=shipper[TYPE], companyName=shipper[COMPANYNAME], checkPoints=shipper[CHECKPOINT], totalCheckPoints=shipper[TOTALCHECKPOINTS], currentCheckPoint=shipper[CURRENTCHECKPOINT])
        else:
            #Large Scale Seller
            if not shipper.__contains__(URLSTATUS) or not shipper.__contains__(TRACKINGURL):
                return Response({'message': FAIL}, 400)
            
            newshipper = Shipper.object.create_shipper(type=shipper[TYPE], companyName=shipper[COMPANYNAME], trackingUrl=shipper[TRACKINGURL], urlStatus=shipper[URLSTATUS])    

        order = order_details.order
        order.shipper_id = newshipper.id

        Order.object.save(order)

    return Response({'message': SUCESS})


@api_view(['PUT'])
@permission_classes([IsAuthenticated, ])
def updateShipper(request, pk):

    data = request.data

    if not data.__contains__(UPDATE):
        return Response({'message': FAIL}, 400)

    user = get_user_for_request(request)

    if not OrderDetails.object.filter(product__shop__userProfile=user, order_id=pk).exists():
        return Response({'message': FAIL}, 404)
    
    order_details = OrderDetails.object.get(product__shop__userProfile=user, order_id=pk)

    if not order_details.order.shipper:
        return Response({'message': FAIL}, 404)
    
    shipper = order_details.order.shipper

    if shipper.type == 1:
        return Response({'message': FAIL}, 400)
    
    shipper.currentCheckPoint = data[UPDATE]
    Shipper.object.save(shipper=shipper)

    return Response({'message': SUCESS}, 200)


     
