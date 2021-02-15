from rest_framework import serializers

from inventory.models import Ingredient, Product, IngredientUsed

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class IngredientUsedSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientUsed
        exclude = ['product']

class ProductSerializer(serializers.ModelSerializer):
    ingredient_used = IngredientUsedSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        ingredient_used = validated_data.pop('ingredient_used')
        product = Product(**validated_data)
        product.save()
        ingredient_used_objs = [
            IngredientUsed(
                ingredient=item['ingredient'],
                quantity_used=item['quantity_used'],
                product=product,
                )
            for item in ingredient_used
            ]
        IngredientUsed.objects.bulk_create(ingredient_used_objs, ignore_conflicts=True)
        return product


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'