from django.urls import path
from .views import *
from django.conf.urls import url,include
from django.views.generic import TemplateView
from django.views.generic import RedirectView
from rest_framework_jwt.views import (obtain_jwt_token,
                                       verify_jwt_token,
                                       refresh_jwt_token)
from rest_framework.urlpatterns import format_suffix_patterns
from rest import views
app_name = "rest"

urlpatterns = [
    
    url('token_refresh/?(?P<user_id>[^/]+)/$', views.RefreshToken.as_view()),
    url('token_verify/?(?P<user_id>[^/]+)/$',views.VerifyToken.as_view()),
    
]