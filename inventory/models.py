from django.db import models

from core.models import TimeStampedMixin

class Ingredient(TimeStampedMixin):
    METRIC_UNIT_CHOICES = (
        ('KG', 'Kilogram'),
        ('L', 'Liter'),
    )
    
    ingredient_name = models.CharField(max_length=255)
    quantity = models.FloatField(default=0)
    metric_unit = models.CharField(choices=METRIC_UNIT_CHOICES, max_length=5, default='kg')

class IngredientUsed(TimeStampedMixin):
    ingredient = models.ForeignKey("inventory.Ingredient", on_delete=models.CASCADE)
    product = models.ForeignKey("inventory.Product", on_delete=models.CASCADE)
    quantity_used = models.FloatField(default=0)

class Product(TimeStampedMixin):
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)
    cost_per_unit = models.FloatField(default=0)

    @property
    def ingredient_used(self):
        return IngredientUsed.objects.filter(product=self)
