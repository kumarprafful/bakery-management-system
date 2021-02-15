from django.urls import path

from inventory import views

urlpatterns = [
    path('ingredient/', views.IngredientView.as_view(), name='ingredient'),
    path('product/', views.ProductView.as_view(), name='product'),
    path('product-list/', views.ProductListView.as_view(), name='product-list'),
    path('hot-selling-products/', views.HotSellingProductListView.as_view(), name='hot-selling-products'),


]
