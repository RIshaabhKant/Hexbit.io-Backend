from django.db import models
from datetime import datetime


from product.models import Product
from order.models import Order


class OrderDetailsManager(models.Manager):
    """Manager for Product"""

    def create_order_details(self, product_id: int, order_id: int, price: int, quantity: int, 
                       total: int, discount=0):
        
        orderDetails = self.model(product_id=product_id, order_id=order_id, price=price,
                                  quantity=quantity, discount=discount, total=total)
        
        self.save(orderDetails=orderDetails)
        
        
    def save(self, orderDetails):
        orderDetails.save(using=self._db)


class OrderDetails(models.Model):
    '''Database model for order details in the system'''

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    price = models.BigIntegerField(null=False)
    quantity = models.BigIntegerField(null=False)
    discount = models.SmallIntegerField(default=0)
    total = models.BigIntegerField(null=False)
    shipedDate = models.DateTimeField(null=True)
    billDate = models.DateTimeField(null=False, default=datetime.now())
    fullfilled = models.BooleanField(default=False)

    object = OrderDetailsManager()

    REQUIRED_FIELD = ['product', 'order', 'price', 'quantity', 'total', 'billDate']

    def __str__(self) -> str:
        orderDetailsVis = f"""product_id: {self.product.id} \n price: {self.price} \n
                        quantity: {self.quantity} \n billDate: {self.billDate} \n"""
        return orderDetailsVis