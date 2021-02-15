from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from inventory.models import Product, IngredientUsed, Ingredient


@receiver(post_save, sender=Ingredient)
def after_ingredient_effects(sender, instance,  created, **kwargs):
    try:
        if created:
            instance.quantity_left = instance.initial_quantity
            instance.save()

    except Exception as e:
        print(e)


@receiver(pre_save, sender=IngredientUsed)
def before_ingredient_used_effects(sender, instance, **kwargs):
    try:
        instance.ingredient.use_ingredient(instance.quantity_used)
    except Exception as e:
        print('exc', e)
        raise e