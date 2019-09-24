from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', views.UserView, basename='Myuser')
router.register('msg', views.MessageView, basename='msg')
router.register('auth_token', views.MyTokenObtainPairView, basename='auth')


urlpatterns = [
    path('', include(router.urls))   
]