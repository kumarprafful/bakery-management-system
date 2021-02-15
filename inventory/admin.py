from django.contrib import admin

from inventory.models import Ingredient, IngredientUsed, Product

admin.site.register(Ingredient)

class IngredientUsedAdmin(admin.TabularInline):
    model = IngredientUsed
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [IngredientUsedAdmin]
    list_display = ['product_name', 'quantity' ,'cost_per_unit']
    