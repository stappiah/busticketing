from django.contrib import admin
from base.models import BusStation, Bus, BusRoute

# Register your models here.
admin.site.register(Bus)
admin.site.register(BusStation)
admin.site.register(BusRoute)