from django.contrib import admin

from buses.models import *

admin.site.register([Bus,Route,BusRoute])



