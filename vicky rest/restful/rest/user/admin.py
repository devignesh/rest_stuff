from django.contrib import admin

from .models import Myuser, Message

# Register your models here.


admin.site.register(Myuser)
admin.site.register(Message)