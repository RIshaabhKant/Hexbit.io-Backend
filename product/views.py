import json


from rest_framework.decorators import api_view
from rest_framework.response import Response


from product.models import Product

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

#Helper Function
def getdataFromRequest(request):
    body = request.body
    return json.loads(body)


#API Functions
@api_view(['GET'])
def getProducts(request):
    '''API to get the product by either shopId or Name or both'''

    data = getdataFromRequest(request)

    if not data.get(NAME) and not data.get(SHOP_ID):
        return Response({'message': FAIL}, 400)
    

    products = []

    if data.get(NAME) and data.get(SHOP_ID):
        products = Product.object.filter(name=data[NAME], shopId=data[SHOP_ID]).values()
    elif data.get(NAME):
        products = Product.object.filter(name=data[NAME]).values()
    else:
        products = Product.object.filter(shopId=data[SHOP_ID]).values()
    

    return Response({'message': SUCESS, 'products': products}, 200)

@api_view(['POST'])
def postProducts(request):
    '''API to create a new product'''

    data = getdataFromRequest(request)

    if not data.__contains__('products'):
        return Response({'message': FAIL}, 400)
    
    products = data['products']

    for product in products:
        if not product.__contains__(NAME) or not product.__contains__(SHOP_ID) or not product.__contains__(SKU) or not product.__contains__(PRICE) or not product.__contains__(DESCRIPTION):
            return Response({'message': FAIL}, 400)
        
        Product.object.create_product(name=product[NAME], shopId=product[SHOP_ID], sku=product[SKU], price=product[PRICE], description=product[DESCRIPTION])
    
    return Response({'message': SUCESS, 'products_add': products}, 200)


@api_view(['PUT'])
def updateProduct(request, pk):
    '''API to update a existing product'''

    if not Product.object.filter(pk=pk).exists():
        return Response({'message': FAIL}, 400)
    
    product = Product.object.get(pk=pk)
    data = getdataFromRequest(request)

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
def deleteProducts(request):
    '''API to delete a existing product'''

    data = getdataFromRequest(request)

    if not data.__contains__(IDS):
        return Response({'message': FAIL}, 400)
    
    products = []

    for id in data[IDS]:
        if not Product.object.filter(pk=id).exists():
            return Response({'message': FAIL}, 400)
        products.append(Product.object.get(pk=id))

    
    for product in products:
        product.delete()
    
    return Response({'message': SUCESS}, 200)