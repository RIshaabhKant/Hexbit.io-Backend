import json

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


from shop.models import Shop

from common.utility.authentication_service import get_user_for_request


#Global Constants
SUCESS = 'Sucess'
FAIL = 'Fail'
PROFILE_ID = 'profileId'
NAME = 'name'
IDS = 'ids'
CITY = 'city'
STATE = 'state'
ACCOUNT_NUMBER = 'accountNumber'
IFSC_CODE = 'ifscCode'
IN_CORPORATION_NAME = 'incorporatioName'
IN_CORPORATION_TYPE = 'incorporationType'
GSTIN = 'gstin'
PAN = 'pan'
PHONE = 'phone'
EMAIL = 'email'


#API Functions
@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def getShops(request):
    ''' API to get shops from profilId '''

    user = get_user_for_request(request=request)
    
    shops = Shop.object.filter(userProfile=user).values()

    return Response({'message': SUCESS, 'shops': shops}, 200)



@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def createShop(request):
    ''' API to create shop '''

    data = request.data

    if not data.__contains__(NAME):
        return Response({'message': FAIL}, 400)
    
    user = get_user_for_request(request=request)

    shop = Shop.object.create_shop(userProfile_id=user.id, name=data[NAME])

    return Response({'message': SUCESS, 'shops': shop.name}, 200)

@api_view(['PUT'])
@permission_classes([IsAuthenticated, ])
def updateShop(request, pk):
    ''' API to update shop '''

    user = get_user_for_request(request=request)

    if not Shop.object.filter(pk=pk, userProfile=user).exists():
        return Response({'message': FAIL}, 404)
    
    shop = Shop.object.get(pk=pk, userProfile=user)
    data = request.data

    if data.__contains__(NAME):
        shop.name = data[NAME]
    if data.__contains__(CITY):
        shop.city = data[CITY]
    if data.__contains__(STATE):
        shop.state = data[STATE]
    if data.__contains__(ACCOUNT_NUMBER):
        shop.accountNumber = data[ACCOUNT_NUMBER]
    if data.__contains__(IFSC_CODE):
        shop.ifscCode = data[IFSC_CODE]
    if data.__contains__(IN_CORPORATION_NAME):
        shop.incorporatioName = data[IN_CORPORATION_NAME]
    if data.__contains__(IN_CORPORATION_TYPE):
        shop.incorporationType = data[IN_CORPORATION_TYPE]
    if data.__contains__(GSTIN):
        shop.gstin = data[GSTIN]
    if data.__contains__(PAN):
        shop.pan = data[PAN]
    if data.__contains__(PHONE):
        shop.phone = data[PHONE]
    if data.__contains__(EMAIL):
        shop.email = data[EMAIL]
    

    Shop.object.save(shop)
    
    
    return Response({'message': SUCESS}, 200)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated, ])
def deleteShops(request):
    '''API to delete a existing product'''

    user = get_user_for_request(request=request)

    data = request.data

    if not data.__contains__(IDS):
        return Response({'message': FAIL}, 400)
    
    products = []

    for id in data[IDS]:
        if not Shop.object.filter(pk=id, userProfile=user).exists():
            return Response({'message': FAIL}, 400)
        products.append(Shop.object.get(pk=id, userProfile=user))

    
    for product in products:
        product.delete()
    
    return Response({'message': SUCESS}, 200)