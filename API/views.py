from rest_framework import viewsets

from API.serializers import ProductSerializer
from Products.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
