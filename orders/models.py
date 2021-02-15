from django.db import models
from django.db.models import Sum
from core.models import TimeStampedMixin


class OrderItem(TimeStampedMixin):
    order = models.ForeignKey("orders.Order", on_delete=models.CASCADE)
    product = models.ForeignKey("inventory.Product", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    cost = models.FloatField(default=0)


class Order(TimeStampedMixin):
    customer = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    total_bill = models.FloatField(default=0)

    @property
    def order_items(self):
        return OrderItem.objects.filter(order=self)

    def __str__(self):
        return str(self.customer)

    def update_total_bill(self):
        order_items = self.order_items
        self.total_bill = order_items.aggregate(Sum('cost')).get('cost__sum')
        self.save()