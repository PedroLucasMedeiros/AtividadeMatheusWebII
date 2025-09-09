from rest_framework import viewsets
from myapp.models import Client
from myapp.models import Product
from myapp.models import Order
from .serializers import ClientSerializer
from .serializers import ProductSerializer
from .serializers import OrderSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer