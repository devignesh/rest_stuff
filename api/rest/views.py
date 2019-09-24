from django.shortcuts import render
from api.settings import SECRET_KEY
from .serializers import TokenSerializer, RefreshSerializer
from rest_framework.response import Response
from rest_framework.views import APIView 
from django.core import serializers
import jwt

# Create your views here.


class VerifyToken(APIView):
    
    serializers_class = TokenSerializer
    def post(self, request, user_id):
        
        serializer = TokenSerializer(data=request.data)
        if serializer.is_valid():
            encode = jwt.encode({'user_id':'1'},  SECRET_KEY, algorithm = 'HS256')
            print(encode)
            decoded = jwt.decode(serializer.validated_data['token'], SECRET_KEY, algorithm = 'HS256')
            result = decoded
            print(result)
            if result['user_id'] == user_id:
                return Response({'msg':'verified'})
            else:
                return Response({'msg':'Invalid token'})
        else:
            return Response({'msg':'Something went wrong'})
        
        