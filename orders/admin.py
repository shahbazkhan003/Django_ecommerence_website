from django.contrib import admin
from orders.models import *


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class OrderItemsAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)  
    
    
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemsAdmin)