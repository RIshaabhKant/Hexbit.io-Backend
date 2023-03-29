from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from django.contrib.auth import get_user_model
from django.http import HttpResponse

# Create your views here.
User = get_user_model()

def Home(request):
    return HttpResponse("hello")

@api_view(['POST'])
def SignUp(request):
    data = request.data
    
    if not data.__contains__('email') or not data.__contains__('password') or not data.__contains__('profile_id') or not data.__contains__('mobile') or not data.__contains__('name') or not data.__contains__('country'):
        return Response({'status': 403, 'message': 'Enter all the fields'})
    
    User.objects.create_user(email=data['email'], password=data['password'], profile_id=data['profile_id'], mobile=data['mobile'], name=data['name'], country=data['country'])
    
    return Response({'status': 200, 'data': data, 'message': 'your message'})

@api_view(['GET'])
def Signin(request):
    data = request.data
    
    if not data.__contains__('email'):
        return Response({'message': "Invalid Field"}, 400)
    
    if not User.objects.filter(email=data['email']).exists():
        return Response({'status': 403, 'message': 'Invalid User'})
    
    user = User.objects.get(email=data['email'])

    if not user.check_password(data['password']):
        return Response({'status': 403, 'message': 'Wrong Password'})
    return Response({'status': 200, 'message': user.id})
    
   
    

