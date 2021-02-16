from django.db import models

from core.models import TimeStampedMixin

class Ingredient(TimeStampedMixin):
    METRIC_UNIT_CHOICES = (
        ('KG', 'Kilogram'),
        ('L', 'Liter'),
    )
    
    ingredient_name = models.CharField(max_length=255, unique=True) #we can also have this unique to track smoothly
    initial_quantity = models.FloatField(default=0)
    quantity_left = models.FloatField(default=0)
    metric_unit = models.CharField(choices=METRIC_UNIT_CHOICES, max_length=5, default='kg')

    def __str__(self):
        return self.ingredient_name
    
    def check_quantity(self, quantity):
        if self.quantity_left >= quantity:
            return True
        else:
            return False

    def use_ingredient(self, quantity):
        if self.check_quantity(quantity):
            self.quantity_left -= quantity
            self.save()
        else:
            raise Exception(f'{self.ingredient_name} : not enough quantity')

class IngredientUsedMananger(models.Manager):
    def bulk_create(self, objs, **kwargs):
        from django.db.models.signals import pre_save
        for item in objs:
            pre_save.send(item.__class__, instance=item)
        return super().bulk_create(objs, **kwargs)

class IngredientUsed(TimeStampedMixin):
    ingredient = models.ForeignKey("inventory.Ingredient", on_delete=models.CASCADE)
    product = models.ForeignKey("inventory.Product", on_delete=models.CASCADE)
    quantity_used = models.FloatField(default=0)

    objects = IngredientUsedMananger()

    def __str__(self):
        return f'{str(self.ingredient)} for {str(self.product)}'
    

class Product(TimeStampedMixin):
    product_name = models.CharField(max_length=255, unique=True) #we can also have this unique to track smoothly
    quantity = models.IntegerField(default=0)
    cost_per_unit = models.FloatField(default=0)
    units_sold = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name
    
    def product_available(self, quantity):
        if self.quantity >= quantity:
            return True
        else:
            return False

    def product_ordered(self, quantity):
        if self.product_available(quantity):
            self.quantity -= quantity
            self.units_sold += quantity
            self.save()
        else:
            raise Exception(f'{self.product_name}: out of stock')

    @property
    def ingredient_used(self):
        return IngredientUsed.objects.filter(product=self)

