from rest_framework import serializers
from rest_framework import authentication
from .models import Myuser, Message, EmailOrMobileAuthBackend
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken


class MyuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Myuser
        fields = ('id','email', 'password', 'first_name', 'last_name', 'mobile')

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        

class MyTokenObtainSerializer(serializers.ModelSerializer):
    username_field = Myuser.email

    def __init__(self, *args, **kwargs):
        super(MyTokenObtainSerializer, self).__init__(*args, **kwargs)

        self.fields[self.username_field] = serializers.CharField()
        self.fields['password'] = serializers.PasswordField()

    def validate(self, attrs):
      
        self.Myuser = Myuser.objects.filter(email=attrs[self.username_field]).first()
        print(self.Myuser)

        if not self.Myuser:
            raise ValidationError('The user is not valid.')

        if self.Myuser:
            if not self.Myuser.check_password(attrs['password']):
                raise ValidationError('Incorrect credentials.')
        print(self.Myuser)
        
        if self.Myuser is None or not self.Myuser.is_active:
            raise ValidationError('No active account found with the given credentials')

        return {}

    @classmethod
    def get_token(cls, Myuser):
        raise NotImplemented(
            'Must implement `get_token` method for `MyTokenObtainSerializer` subclasses')


class MyTokenObtainPairSerializer(MyTokenObtainSerializer):
    @classmethod
    def get_token(cls, Myuser):
        return RefreshToken.for_user(Myuser)

    def validate(self, attrs):
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)

        refresh = self.get_token(self.Myuser)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data
        
        
#class MyuserLoginSerializer(serializers.ModelSerializer):
    #token = CharField(allow_blank=True, read_only=True)
    #email = EmailField(label='Email Address', required=False, allow_blank=True)
    #class Meta:
     #   model = Myuser
      #  fields = [
       #     'email',
        #    'password',
         #   'token',
        #]
        
        #extra_kwargs = {"password": {"write_only": True}}
        
    #def validate(self, data):
     #   email = data.get("email", None)
      #  if not email:
       #     raise ValidationError("Email is required one")
        #
        #myuser = Mysuer.objects.filter(
         #   Q(email=email)
            
        #).distinct()
        
        #return data        
    
