import json


from rest_framework.decorators import api_view
from rest_framework.response import Response


from shop.models import Shop


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


#Helper Function
def getdataFromRequest(request):
    body = request.body
    return json.loads(body)


#API Functions
@api_view(['GET'])
def getShops(request):
    ''' API to get shops from profilId '''

    data = getdataFromRequest(request)
    
    if not data.__contains__(PROFILE_ID):
        return Response({'message': FAIL}, 400)
    
    if not Shop.object.filter(profileId=data[PROFILE_ID]).exists():
        return Response({'message': FAIL}, 400)
    
    shops = Shop.object.filter(profileId=data[PROFILE_ID]).values()

    return Response({'message': SUCESS, 'shops': shops}, 200)



@api_view(['POST'])
def createShop(request):
    ''' API to create shop '''

    data = getdataFromRequest(request)

    if not data.__contains__(PROFILE_ID) or not data.__contains__(NAME):
        return Response({'message': FAIL}, 400)
    
    shop = Shop.object.create_shop(profileId=data[PROFILE_ID], name=data[NAME])

    return Response({'message': SUCESS, 'shops': shop.name}, 200)

@api_view(['PUT'])
def updateShop(request, pk):
    ''' API to update shop '''

    if not Shop.object.filter(pk=pk).exists():
        return Response({'message': FAIL}, 400)
    
    shop = Shop.object.get(pk=pk)
    data = getdataFromRequest(request)

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
def deleteShops(request):
    '''API to delete a existing product'''

    data = getdataFromRequest(request)

    if not data.__contains__(IDS):
        return Response({'message': FAIL}, 400)
    
    products = []

    for id in data[IDS]:
        if not Shop.object.filter(pk=id).exists():
            return Response({'message': FAIL}, 400)
        products.append(Shop.object.get(pk=id))

    
    for product in products:
        product.delete()
    
    return Response({'message': SUCESS}, 200)