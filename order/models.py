from django.db import models
from datetime import datetime


from payment.models import Payment
from shipper.models import Shipper

class OrderManager(models.Manager):
    """Manager for Order"""

    def create_order(self, customer_id: int, payment_id: int, shipper_id: int, paid:int, transactionStatus=0, 
                     paymentDate=None):
        order = self.model(customer_id=customer_id, payment_id=payment_id, shipper_id=shipper_id, 
                           paid=paid, transactionStatus=transactionStatus, paymentDate=paymentDate)
        
        self.save(order=order)
        return order
        
        
    def save(self, order):
        order.save(using=self._db)
    


class Order(models.Model):
    '''Database model for orders in the system'''

    customer_id = models.BigIntegerField(unique=True) #TODO: Change to ForeignKey for Customer
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    shipper = models.ForeignKey(Shipper, on_delete=models.CASCADE, null=True)

    orderDate = models.DateField(auto_now_add=True, blank=True)
    timestamp =  models.TimeField(auto_now_add=True, blank=True)
    transactionStatus = models.SmallIntegerField(default=0)
    ErrorMessage = models.CharField(max_length=255)
    paymentDate = models.DateField()
    paid = models.BigIntegerField(max_length=200)
    fullFilled = models.BooleanField(default=False)


    object = OrderManager()


    def __str__(self) -> str:
        orderVis = f"orderId: {self.pk}, orderDate: {self.orderDate}"
        return orderVis



