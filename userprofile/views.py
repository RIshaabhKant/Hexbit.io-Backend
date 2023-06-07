from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from common.utility.authentication_service import get_tokens_for_user, get_access_from_refresh_token

# Create your views here.
User = get_user_model()


NAME = 'name'
EMAIL = 'email'
FAIL = 'Fail'
PASSWORD = 'password'
MOBILE = 'mobile'
COUNTRY = 'country'
PAN = 'pan_number'
INCORPORATION = 'incorporation_type'
FSSAI = 'fssai_number'
BANK = 'bank_account'
ACCOUNT = 'account_number'
IFSC = 'ifsc_code'
GST = 'gst_number'
LEGAL = 'legal_entity_name'
TOKEN = 'token'


@api_view(['POST'])
@permission_classes([AllowAny, ])
def SignUp(request):
    data = request.data

    if not data.__contains__(EMAIL) or not data.__contains__(PASSWORD) or not data.__contains__(PAN) or not data.__contains__(MOBILE) or not data.__contains__(NAME) or not data.__contains__(COUNTRY) or not data.__contains__(INCORPORATION) or not data.__contains__(FSSAI) or not data.__contains__(BANK) or not data.__contains__(ACCOUNT) or not data.__contains__(IFSC) or not data.__contains__(GST) or not data.__contains__(LEGAL):
        return Response({'message': 'Enter all the fields'}, 403)

    user = User.objects.create_user(email=data[EMAIL], password=data[PASSWORD], pan_number=data[PAN], mobile=data[MOBILE], name=data[NAME], country=data[COUNTRY], incorporation_type=data[INCORPORATION],
                                    fssai_number=data[FSSAI], bank_account=data[BANK], account_number=data[ACCOUNT], ifsc_code=data[IFSC], gst_number=data[GST], legal_entity_name=data[LEGAL])
    token = get_tokens_for_user(user=user)

    return Response({'data': data, 'message': user.id, 'token': token}, 200)


@api_view(['GET'])
@permission_classes([AllowAny, ])
def Signin(request):
    data = request.data

    if not data.__contains__(EMAIL):
        return Response({'message': "Invalid Field"}, 400)

    if not User.objects.filter(email=data[EMAIL]).exists():
        return Response({'message': 'Invalid User'}, 403)

    user = User.objects.get(email=data[EMAIL])

    if not user.check_password(data[PASSWORD]):
        return Response({'message': 'Wrong Password'}, 403)

    token = get_tokens_for_user(user=user)

    return Response({'message': user.id, "token": token}, 200)


@api_view(['GET'])
@permission_classes([AllowAny, ])
def getAccess(request):
    data = request.data

    if not data.__contains__(TOKEN):
        return Response({'message': "Invalid Field"}, 400)

    token = get_access_from_refresh_token(data[TOKEN])

    status_code = 200
    if token.__contains__('error'):
        status_code = 400

    return Response({"token": token}, status_code)
