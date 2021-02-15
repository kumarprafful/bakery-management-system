from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsBakeryAdminAuthenticated, IsCustomerAuthenticated

from inventory.serializers import IngredientSerializer, ProductSerializer, ProductListSerializer
from inventory.models import Ingredient, Product

from core.pagination import CursorPagination

class IngredientView(APIView):
    permission_classes = [IsBakeryAdminAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            data = JSONParser().parse(request)

            serializer = IngredientSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response({'status': 'error', 'message': serializer.errors}, status=400)
            return Response({'status': 'success', 'data': serializer.data}, status=201)
        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=400)

    def get(self, request, *args, **kwargs):
        try:
            ingredient = Ingredient.objects.get(id=request.GET.get('ingredient_id'))
            serializer = IngredientSerializer(instance=ingredient)
            return Response({'status': 'success', 'data': serializer.data}, status=200)
        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=400)
    
    def put(self, request, *args, **kwargs):
        try:
            data = JSONParser().parse(request)
            ingredient = Ingredient.objects.get(id=data.get('ingredient_id'))
            serializer = IngredientSerializer(instance=ingredient, data=data, partial=True)

            if serializer.is_valid():
                serializer.save()
            else:
                return Response({'status': 'error', 'message': serializer.errors}, status=400)
            return Response({'status': 'success', 'data': serializer.data}, status=200)
        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=400)
    
    def delete(self, request, *args, **kwargs):
        try:
            ingredient = Ingredient.objects.get(id=request.GET.get('ingredient_id'))
            ingredient.delete()
            return Response({'status': 'success',}, status=204)
        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=400)


class ProductView(APIView):
    permission_classes = [IsBakeryAdminAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            data = JSONParser().parse(request)

            serializer = ProductSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response({'status': 'error', 'message': serializer.errors}, status=400)
            return Response({'status': 'success', 'data': serializer.data}, status=201)
        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=400)

    def get(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(id=request.GET.get('product_id'))
            serializer = ProductSerializer(instance=product)
            return Response({'status': 'success', 'data': serializer.data}, status=200)
        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=400)
    
    def put(self, request, *args, **kwargs):
        try:
            data = JSONParser().parse(request)
            product = Product.objects.get(id=data.get('product_id'))
            serializer = ProductSerializer(instance=product, data=data, partial=True)

            if serializer.is_valid():
                serializer.save()
            else:
                return Response({'status': 'error', 'message': serializer.errors}, status=400)
            return Response({'status': 'success', 'data': serializer.data}, status=200)
        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=400)
    
    def delete(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(id=request.GET.get('product_id'))
            product.delete()
            return Response({'status': 'success',}, status=204)
        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=400)

class ProductListView(ListAPIView):
    serializer_class = ProductListSerializer
    pagination_class = CursorPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.objects.all().order_by('-quantity')


class HotSellingProductListView(ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.objects.all().order_by('-units_sold')[:10]