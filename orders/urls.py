from django.urls import path

from orders import views

urlpatterns = [
    path('order/', views.OrderView.as_view(), name='order'),
    path('order-history/', views.OrderHistoryView.as_view(), name='order-history'),
    
]
