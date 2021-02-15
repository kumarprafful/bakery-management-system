from django.contrib import admin

from orders.models import Order, OrderItem

class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemAdmin]

