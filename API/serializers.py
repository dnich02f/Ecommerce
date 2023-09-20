# In the API app, you can create serializers and views to expose the existing models through RESTful endpoints.
# You may not need additional models specific to the API app.

# Example serializer and view in the API app:
from rest_framework import serializers
from Products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
