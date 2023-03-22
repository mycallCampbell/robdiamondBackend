from rest_framework import serializers
from .models import Product, Blog


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"
