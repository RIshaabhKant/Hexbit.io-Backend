from django.db import models


from shop.models import Shop


class ProductManager(models.Manager):
    """Manager for Product"""

    def create_product(self, name: str, sku: int, price: int, shop_id: int, description: str, 
                       discount=0, unitsInStock=0, size=0, colour=0, unitWeight=0):
        


        product = self.model(name=name, sku=sku, shop_id=shop_id, description=description, price=price,
                             discount=discount, unitsInStock=unitsInStock, size=size,colour=colour, 
                             unitWeight=unitWeight)
        
        self.save(product=product)

        return product
    
    def save(self, product):
        product.save(using=self._db)
        


class Product(models.Model):
    '''Database model for products in the system'''

    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    name = models.CharField(max_length=255, null=False)
    sku = models.BigIntegerField(null=False)
    isActive = models.BooleanField(default=False)
    price = models.DecimalField(default=0, decimal_places=4, max_digits=10)
    description = models.CharField(max_length=1000, null=False)
    discount = models.SmallIntegerField(default=0)
    unitsInStock = models.BigIntegerField(default=0)
    totalUnitsOrder = models.BigIntegerField(default=0)
    size = models.SmallIntegerField(default=0)
    colour = models.SmallIntegerField(default=0)
    unitWeight = models.BigIntegerField(default=0)
    
    #TODE:
    '''
    Add image url, availableSize, availableColour field
    '''

    object = ProductManager()
    REQUIRED_FIELD = ['name']


    def __str__(self) -> str:
        productVis = f"""Name: {self.name} \n shopId: {self.shop.id} \n price: {self.price} \n 
                        UnitInStock: {self.unitsInStock} \n Description: {self.description} \n"""
        return productVis

