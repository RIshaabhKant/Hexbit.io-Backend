from datetime import datetime
import json

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from order_details.models import OrderDetails
from payment.serializers import PaymentSerializer

from common.utility.authentication_service import get_user_for_request


SUCESS = 'Sucess'
FAIL = 'Fail'


#API Functions
@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def getPayments(request, pk):

    user = get_user_for_request(request)
    payments = []

    if OrderDetails.object.filter(product__shop__userProfile=user, product__shop=pk).exists():
        order_details = OrderDetails.object.filter(product__shop__userProfile=user, product__shop=pk).all()

        for order_detail in order_details:
            _payment = PaymentSerializer(order_detail.order.payment)
            bytesString = json.dumps(_payment.data)
            payment = json.loads(bytesString)
            payments.append(payment)

    return Response({'message': SUCESS, 'paymests': payments})
