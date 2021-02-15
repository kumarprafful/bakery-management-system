from rest_framework import serializers
from orders.models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class  Meta:
        model = OrderItem
        exclude = ['order',]

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
        # order_item_objs = [
        #     OrderItem(
        #         order=order,
        #         product=item['product'],
        #         quantity=item['quantity']
        #     )
        #     for item in order_items
        # ]
        # OrderItem.objects.bulk_create(order_item_objs)
        return order