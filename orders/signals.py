from django.db.models.signals import post_save, pre_save
from django.db.models import Sum
from django.dispatch import receiver
from orders.models import Order, OrderItem


@receiver(pre_save, sender=OrderItem)
def before_order_item_effects(sender, instance, **kwargs):
    instance.product.product_ordered(instance.quantity)
    instance.cost = instance.product.cost_per_unit * instance.quantity

@receiver(post_save, sender=OrderItem)
def after_order_item_effects(sender, instance, **kwargs):
    instance.order.update_total_bill()