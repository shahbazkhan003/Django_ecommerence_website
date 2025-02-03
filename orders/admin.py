from django.contrib import admin
from orders.models import *


class OrderPlacedAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class OrderItemsAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)  
    
    
admin.site.register(OrderPlaced, OrderPlacedAdmin)
admin.site.register(OrderItems, OrderItemsAdmin)