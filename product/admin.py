from django.contrib import admin
from .models import Item, Order

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']
    list_filter = ['price']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'total_amount', 'order_number', ]

