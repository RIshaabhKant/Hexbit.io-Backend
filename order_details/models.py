from django.db import models
from datetime import datetime


class OrderDetailsManager(models.Manager):
    """Manager for Product"""

    def create_order_details(self, productId: int, orderId: int, price: int, quantity: int, 
                       total: int, discount=0):
        
        orderDetails = self.model(productId=productId, orderId=orderId, price=price,
                                  quantity=quantity, discount=discount, total=total)
        
        self.save(orderDetails=orderDetails)
        
        
    def save(self, orderDetails):
        orderDetails.save(using=self._db)


class OrderDetails(models.Model):
    '''Database model for order details in the system'''

    productId = models.BigIntegerField(null=False) #TODO: Change to ForeignKey
    orderId = models.BigIntegerField(null=False) #TODO: Change to ForeignKey

    price = models.BigIntegerField(null=False)
    quantity = models.BigIntegerField(null=False)
    discount = models.SmallIntegerField(default=0)
    total = models.BigIntegerField(null=False)
    shipedDate = models.DateTimeField(null=True)
    billDate = models.DateTimeField(null=False, default=datetime.now())
    fullfilled = models.BooleanField(default=False)

    object = OrderDetailsManager()

    REQUIRED_FIELD = ['productId', 'orderID', 'price', 'quantity', 'total', 'billDate']

    def __str__(self) -> str:
        orderDetailsVis = f"""productId: {self.productId} \n price: {self.price} \n
                        quantity: {self.quantity} \n billDate: {self.billDate} \n"""
        return orderDetailsVis