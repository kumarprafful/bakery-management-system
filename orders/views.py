from accounts.permissions import (IsBakeryAdminAuthenticated,
                                  IsCustomerAuthenticated)
from core.pagination import CursorPagination
from rest_framework.generics import ListAPIView
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from orders.models import Order
from orders.serializers import OrderSerializer


class OrderView(APIView):
    permission_classes = [IsCustomerAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            data = JSONParser().parse(request)
            print(data, type(data))
            data['customer'] = request.user.id
            serializer = OrderSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response({'status': 'error', 'message': serializer.errors}, status=400)
            return Response({'status': 'success', 'data': serializer.data}, status=200)
        except Exception as e:
            return Response({'status': 'error', 'errors': str(e)}, status=400)
            
class OrderHistoryView(ListAPIView):
    permission_classes = [IsCustomerAuthenticated]
    serializer_class = OrderSerializer
    pagination_class = CursorPagination

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)
