from rest_framework import serializers
from orders.models import Order, OrderItem
from inventory.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name',]

class OrderItemSerializer(serializers.ModelSerializer):
    # product = ProductSerializer(required=False, read_only=True)
    product_name = serializers.SerializerMethodField()
    class  Meta:
        model = OrderItem
        exclude = ['order', 'created', 'updated', 'id',]

    def get_product_name(self, obj):
        return obj.product.product_name

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, required=False)
    class Meta:
        model = Order
        fields = '__all__'
    
    def create(self, validated_data):
        order_items = validated_data.pop('order_items')
        order = Order(**validated_data)
        order.save()
        [
           OrderItem.objects.create(
               order=order,
               product=item['product'],
               quantity=item['quantity']
           )
           for item in order_items
        ]
        return order