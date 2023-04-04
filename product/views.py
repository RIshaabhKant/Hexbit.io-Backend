import json


from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


from product.models import Product
from shop.models import Shop
from userprofile.models import UserProfile


from common.utility.authentication_service import get_user_for_request

#Global Constants
NAME = 'name'
SUCESS = 'Sucess'
FAIL = 'Fail'
SHOP_ID = 'shopId'
SKU = 'sku'
PRICE = 'price'
DESCRIPTION = 'description'
DISCOUNT = 'discount'
UNIT_IN_STOCK = 'unitsInStock'
SIZE = 'size'
COLOUR = 'colour'
UNIT_WEIGHT = 'unitWeight'
IDS = 'ids'


#API Functions
@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def getProducts(request):
    '''API to get the product by either shopId or Name or both'''

    user = get_user_for_request(request=request)

    data = request.data

    products = []

    if data.__contains__(NAME):
        products = Product.object.filter(name=data[NAME], shop__userProfile=user).values()
    else:
        products = Product.object.filter(shop__userProfile=user).values()
    

    return Response({'message': SUCESS, 'products': products}, 200)

@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def postProducts(request):
    '''API to create a new product'''

    user = get_user_for_request(request=request)

    data = request.data

    if not data.__contains__('products'):
        return Response({'message': FAIL}, 400)
    
    products = data['products']

    for product in products:
        if not product.__contains__(NAME) or not product.__contains__(SHOP_ID) or not product.__contains__(SKU) or not product.__contains__(PRICE) or not product.__contains__(DESCRIPTION):
            return Response({'message': FAIL}, 400)
        
        if not Shop.object.filter(pk=product[SHOP_ID], userProfile=user).exists():
            return Response({'message': FAIL}, 404)

    for product in products:
        Product.object.create_product(name=product[NAME], shop_id=product[SHOP_ID], sku=product[SKU], price=product[PRICE], description=product[DESCRIPTION])
    
    return Response({'message': SUCESS}, 200)


@api_view(['PUT'])
@permission_classes([IsAuthenticated, ])
def updateProduct(request, pk):
    '''API to update a existing product'''

    user = get_user_for_request(request=request)
    data = request.data

    if not Product.object.filter(pk=pk, shop__userProfile=user).exists():
        return Response({'message': FAIL}, 404)
    
    
    product = Product.object.get(pk=pk, shop__userProfile=user)

    if data.__contains__(NAME):
        product.name = data[NAME]
    if data.__contains__(SKU):
        product.sku = data[SKU]
    if data.__contains__(PRICE):
        product.price = data[PRICE]
    if data.__contains__(DESCRIPTION):
        product.description = data[DESCRIPTION]
    if data.__contains__(DISCOUNT):
        product.discount = data[DISCOUNT]
    if data.__contains__(UNIT_IN_STOCK):
        product.unitsInStock = data[UNIT_IN_STOCK]
    if data.__contains__(SIZE):
        product.size = data[SIZE]
    if data.__contains__(COLOUR):
        product.colour = data[COLOUR]
    if data.__contains__(UNIT_WEIGHT):
        product.unitWeight = data[UNIT_WEIGHT]
    
    
    Product.object.save(product)
    
    
    return Response({'message': SUCESS}, 200)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated, ])
def deleteProducts(request):
    '''API to delete a existing product'''

    user = get_user_for_request(request=request)
    data = request.data

    if not data.__contains__(IDS):
        return Response({'message': FAIL}, 400)
    
    products = []

    for id in data[IDS]:
        if not Product.object.filter(pk=id, shop__userProfile=user).exists():
            return Response({'message': FAIL}, 404)
        products.append(Product.object.get(pk=id, shop__userProfile=user))

    
    for product in products:
        product.delete()
    
    return Response({'message': SUCESS}, 200)