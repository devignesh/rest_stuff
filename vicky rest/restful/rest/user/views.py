from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Myuser, Message
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyuserSerializer, MessageSerializer, MyTokenObtainPairSerializer 
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,get_authorization_header, BaseAuthentication

# Create your views here.

class UserView(viewsets.ModelViewSet):
    queryset = Myuser.objects.all()
    serializer_class = MyuserSerializer

class MessageView(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    
    
class MyTokenObtainPairView(viewsets.ModelViewSet):
       
    serializer_class = MyTokenObtainPairSerializer
    
