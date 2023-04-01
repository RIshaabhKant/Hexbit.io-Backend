from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from django.contrib.auth import get_user_model
from django.http import HttpResponse

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

@api_view(['POST'])
def SignUp(request):
    data = request.data
    
    if not data.__contains__(EMAIL) or not data.__contains__(PASSWORD) or not data.__contains__(PAN) or not data.__contains__(MOBILE) or not data.__contains__(NAME) or not data.__contains__(COUNTRY) or not data.__contains__(INCORPORATION) or not data.__contains__(FSSAI) or not data.__contains__(BANK) or not data.__contains__(ACCOUNT) or not data.__contains__(IFSC) or not data.__contains__(GST) or not data.__contains__(LEGAL):
        return Response({'status': 403, 'message': 'Enter all the fields'})
    
    User.objects.create_user(email=data[EMAIL], password=data[PASSWORD], pan_number=data[PAN], mobile=data[MOBILE], name=data[NAME], country=data[COUNTRY], incorporation_type = data[INCORPORATION], fssai_number= data[FSSAI], bank_account=data[BANK], account_number=data[ACCOUNT], ifsc_code=data[IFSC], gst_number= data[GST], legal_entity_name=data[LEGAL])
    
    return Response({'status': 200, 'data': data, 'message': 'User Created !'})

@api_view(['GET'])
def Signin(request):
    data = request.data
    
    if not data.__contains__(EMAIL):
        return Response({'message': "Invalid Field"}, 400)
    
    if not User.objects.filter(email=data[EMAIL]).exists():
        return Response({'status': 403, 'message': 'Invalid User'})
    
    user = User.objects.get(email=data[EMAIL])

    if not user.check_password(data[PASSWORD]):
        return Response({'status': 403, 'message': 'Wrong Password'})
    return Response({'status': 200, 'message': user.id})
    
   
    

